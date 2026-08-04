import json, csv
from collections import defaultdict
from pathlib import Path

VALID = {"MET","PARTIALLY_MET","NOT_MET","CONTRADICTED","NOT_ASSESSABLE"}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_ledger(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate_framework(fw):
    assert fw["framework_version"] == "0.2"
    assert fw["status"] == "FROZEN_FOR_DOWNSTREAM_TESTING"


def family_counts(rows):
    by_domain=defaultdict(set)
    for r in rows:
        by_domain[r["domain"]].add(r["study_family_id"])
    return {k:len(v) for k,v in sorted(by_domain.items())}


def validate_judgments(j):
    for track, classes in j["tracks"].items():
        for cls, payload in classes.items():
            for code, item in payload["criteria"].items():
                if item["status"] not in VALID:
                    raise ValueError(f"Invalid status {track} {cls} {code}")


def gate_class(framework, class_name, criterion_payload):
    spec=framework["classification_specific_criteria"][class_name]
    criteria=criterion_payload["criteria"]
    required=spec.get("required",[])
    statuses={c:criteria.get(c,{"status":"NOT_ASSESSABLE"})["status"] for c in required}
    if any(s in {"NOT_MET","CONTRADICTED"} for s in statuses.values()):
        gate="NOT_SUPPORTED_AS_GLOBAL_CLASS"
    elif all(s=="MET" for s in statuses.values()):
        gate="SUPPORTED"
    elif all(s in {"MET","PARTIALLY_MET"} for s in statuses.values()):
        gate="PARTIALLY_SUPPORTED"
    else:
        gate="INSUFFICIENT_EVIDENCE"
    return gate, statuses


def run(framework_path, config_path, ledger_path, judgments_path, outdir):
    fw=load_json(framework_path); validate_framework(fw)
    cfg=load_json(config_path)
    ledger=load_ledger(ledger_path)
    j=load_json(judgments_path); validate_judgments(j)
    out=Path(outdir); out.mkdir(parents=True, exist_ok=True)

    summary={
        "module_version":cfg["version"],
        "historical_framework_version":fw["framework_version"],
        "historical_framework_immutable":cfg["historical_framework_immutable"],
        "records":len(ledger),
        "unique_study_families":len(set(r["study_family_id"] for r in ledger)),
        "domains":family_counts(ledger),
        "tracks":{}
    }
    for track, classes in j["tracks"].items():
        summary["tracks"][track]={}
        for cls, payload in classes.items():
            gate, req=gate_class(fw, cls, payload)
            summary["tracks"][track][cls]={"gate":gate,"required_criteria":req,"interpretation":payload["interpretation"]}

    h=summary["tracks"]["HIGHER_CONFIDENCE_EVIDENCE"]
    supported=[k for k,v in h.items() if v["gate"] in {"SUPPORTED","PARTIALLY_SUPPORTED"}]
    summary["preferred_formulation"]="COMPOSITE_MULTIAXIAL" if len(supported)>=2 else (supported[0] if supported else "INSUFFICIENT_EVIDENCE")
    summary["supported_or_partial_classes"]=supported

    with open(out/"run_summary.json","w",encoding="utf-8") as f: json.dump(summary,f,indent=2)
    return summary
