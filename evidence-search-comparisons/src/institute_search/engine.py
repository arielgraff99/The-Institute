from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Iterable
from uuid import uuid4

from .config import RunConfig
from .graph import EvidenceGraph
from .novelty import NoveltyHook, normalize_insights
from .state import CycleAudit, RunState


class EvidenceSearchEngine:
    """Reusable orchestration kernel.

    Search providers, LLMs, scientific ontologies, and disease-specific extractors
    are intentionally outside this class. They feed normalized cycle payloads into
    the kernel, which handles provenance, novelty, saturation, graph state,
    integrity ledgers, and reproducible run outputs.
    """

    def __init__(self, config: RunConfig, novelty_hooks: Iterable[NoveltyHook] = ()) -> None:
        self.config = config
        self.hooks = list(novelty_hooks)
        self.graph = EvidenceGraph()
        self.state = RunState(run_id=uuid4().hex[:12], project_id=config.project_id)
        self.risk_of_bias_rows: list[dict[str, Any]] = []
        self.negative_evidence_rows: list[dict[str, Any]] = []
        self.missing_evidence_rows: list[dict[str, Any]] = []
        self.registry_match_rows: list[dict[str, Any]] = []
        self.replication_rows: list[dict[str, Any]] = []

    @staticmethod
    def _material_integrity_insights(payload: dict[str, Any]) -> list[dict[str, Any]]:
        """Promote material negative/missing evidence to scientific novelty.

        This prevents a caller from accidentally allowing the saturation streak to
        continue after a new null result, failed replication, unpublished completed
        study, missing registered outcome, or other material missing-evidence signal.
        """
        out: list[dict[str, Any]] = []
        for item in payload.get("negative_evidence", []):
            if item.get("material", True) is False:
                continue
            provenance = [str(x) for x in item.get("provenance", []) if str(x).strip()]
            summary = str(item.get("summary", "")).strip()
            if not provenance or not summary:
                continue
            finding_type = str(item.get("finding_type", "negative_evidence")).strip() or "negative_evidence"
            out.append({
                "category": f"negative_evidence:{finding_type}",
                "summary": summary,
                "provenance": provenance,
                "material": True,
            })
        for item in payload.get("missing_evidence_signals", []):
            if item.get("material", True) is False:
                continue
            provenance = [str(x) for x in item.get("provenance", []) if str(x).strip()]
            description = str(item.get("description", "")).strip()
            if not provenance or not description:
                continue
            signal_type = str(item.get("signal_type", "missing_evidence")).strip() or "missing_evidence"
            out.append({
                "category": f"missing_evidence:{signal_type}",
                "summary": description,
                "provenance": provenance,
                "material": True,
            })
        return out

    def ingest_cycle(self, payload: dict[str, Any]) -> CycleAudit:
        generation = int(payload["generation_number"])
        raw_insights = list(payload.get("novel_insights", []))
        raw_insights.extend(self._material_integrity_insights(payload))
        for hook in self.hooks:
            raw_insights.extend(
                {
                    "category": x.category,
                    "summary": x.summary,
                    "provenance": x.provenance,
                    "material": x.material,
                }
                for x in hook.evaluate(payload)
            )
        insights = normalize_insights(raw_insights)

        self.risk_of_bias_rows.extend(dict(x) for x in payload.get("risk_of_bias", []))
        self.negative_evidence_rows.extend(dict(x) for x in payload.get("negative_evidence", []))
        self.missing_evidence_rows.extend(dict(x) for x in payload.get("missing_evidence_signals", []))
        self.registry_match_rows.extend(dict(x) for x in payload.get("registry_publication_matches", []))
        self.replication_rows.extend(dict(x) for x in payload.get("replication_map", []))

        for node in payload.get("nodes", []):
            record_id = str(node["record_id"])
            attrs = dict(node)
            attrs.pop("record_id", None)
            attrs.setdefault("generation", generation)
            self.graph.add_record(record_id, **attrs)
        for edge in payload.get("edges", []):
            attrs = dict(edge)
            source = str(attrs.pop("source"))
            target = str(attrs.pop("target"))
            self.graph.add_discovery_edge(source, target, **attrs)
        for pruning in payload.get("pruning", []):
            self.graph.prune(str(pruning["record_id"]), str(pruning["reason"]))

        audit = CycleAudit(
            cycle_id=str(payload.get("cycle_id", f"cycle-{generation}")),
            generation_number=generation,
            novel_insights=[
                {"category": i.category, "summary": i.summary, "provenance": i.provenance}
                for i in insights
            ],
            new_records_count=len(payload.get("nodes", [])),
            new_study_families_count=int(payload.get("new_study_families_count", 0)),
            pruned_nodes_count=len(payload.get("pruning", [])),
            tokens=payload.get("tokens"),
            cost=payload.get("cost"),
        )
        self.state.register_cycle(audit)
        self.state.status = self._decision()
        return audit

    def _decision(self) -> str:
        sat = self.config.saturation
        if len(self.state.cycles) < sat.minimum_recursive_generations:
            return "CONTINUE"
        if self.state.consecutive_zero_novel_insight_cycles >= sat.minimum_consecutive_zero_novel_insight_cycles:
            return "SATURATION_CANDIDATE"
        return "CONTINUE"

    def resource_limited_stop(self, reason: str) -> None:
        self.state.metadata["resource_stop_reason"] = reason
        self.state.status = "RESOURCE_LIMITED_NOT_SATURATED"

    @staticmethod
    def _write_csv(path: Path, rows: list[dict[str, Any]], default_fields: list[str]) -> None:
        fields = list(default_fields)
        for row in rows:
            for key in row:
                if key not in fields:
                    fields.append(key)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                normalized = {
                    key: json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict, tuple)) else value
                    for key, value in row.items()
                }
                writer.writerow(normalized)

    def write_run(self, output_dir: str | Path) -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "resolved_config.json").write_text(self.config.model_dump_json(indent=2), encoding="utf-8")
        (out / "saturation_trace.json").write_text(json.dumps(self.state.to_dict(), indent=2), encoding="utf-8")
        self.graph.write_graphml(out / "citation_graph.graphml")
        self.graph.render_dot(out / "growth_and_pruning.dot")
        self.graph.render_dot(out / "growth_and_pruning_study_family.dot", compressed_by_study_family=True)

        self._write_csv(
            out / "risk_of_bias.csv",
            self.risk_of_bias_rows,
            ["study_id", "result_id", "design", "tool", "overall_judgment", "rationale"],
        )
        self._write_csv(
            out / "negative_evidence_ledger.csv",
            self.negative_evidence_rows,
            ["source_id", "study_family_id", "finding_type", "claim_id", "summary", "material", "provenance"],
        )
        self._write_csv(
            out / "publication_bias_audit.csv",
            self.missing_evidence_rows,
            ["signal_type", "source_id", "description", "material", "confidence", "provenance"],
        )
        self._write_csv(
            out / "registry_publication_matches.csv",
            self.registry_match_rows,
            ["registry_id", "publication_id", "missing_registered_outcomes", "unregistered_reported_outcomes", "sample_size_delta", "completed_without_publication"],
        )
        missing_outcomes = [row for row in self.registry_match_rows if row.get("missing_registered_outcomes")]
        self._write_csv(
            out / "missing_outcomes.csv",
            missing_outcomes,
            ["registry_id", "publication_id", "missing_registered_outcomes"],
        )
        self._write_csv(
            out / "replication_map.csv",
            self.replication_rows,
            ["publication_id", "study_family_id", "cohort_id", "dataset_id", "laboratory_id", "pipeline_id"],
        )
        return out
