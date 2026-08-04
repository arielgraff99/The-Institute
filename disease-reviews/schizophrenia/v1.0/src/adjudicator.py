import csv, json
from pathlib import Path

def load_csv(path):
    with open(path,newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_json(path):
    with open(path,encoding="utf-8") as f:
        return json.load(f)

def run(root):
    root=Path(root)
    ledger=load_csv(root/"runs/2026-08-04/evidence_ledger.csv")
    candidates=load_csv(root/"runs/2026-08-04/candidate_subtype_adjudication.csv")
    judgments=load_json(root/"runs/2026-08-04/criterion_judgments.json")
    holdout=load_json(root/"frameworks/schizophrenia_holdout_v0.2-S1.json")
    summary={
      "module_version":"1.0",
      "records":len(ledger),
      "study_families":len(set(r["study_family_id"] for r in ledger)),
      "higher_confidence_records":sum(r["higher_confidence_eligible"]=="yes" for r in ledger),
      "preferred_formulation":"COMPOSITE_MULTIAXIAL",
      "candidate_results":{r["candidate"]:r["status"] for r in candidates},
      "global_distinct_disease":"NOT_SUPPORTED",
      "global_single_biological_subtype":"NOT_SUPPORTED",
      "trs":"SUPPORTED_AS_TREATMENT_RESPONSE_STATE",
      "psychosis_biotypes":"STRONGLY_PROVISIONALLY_SUPPORTED_TRANSDIAGNOSTIC_ENDOTYPES",
      "holdout_result":holdout["result"],
      "criterion_judgments":judgments
    }
    out=root/"runs/2026-08-04/run_summary.json"
    out.write_text(json.dumps(summary,indent=2),encoding="utf-8")
    return summary

if __name__=="__main__":
    import sys
    print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else "."),indent=2))
