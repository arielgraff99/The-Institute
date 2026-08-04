from __future__ import annotations

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
    the kernel, which handles provenance, novelty, saturation, graph state, and
    reproducible run outputs.
    """

    def __init__(self, config: RunConfig, novelty_hooks: Iterable[NoveltyHook] = ()) -> None:
        self.config = config
        self.hooks = list(novelty_hooks)
        self.graph = EvidenceGraph()
        self.state = RunState(run_id=uuid4().hex[:12], project_id=config.project_id)

    def ingest_cycle(self, payload: dict[str, Any]) -> CycleAudit:
        generation = int(payload["generation_number"])
        raw_insights = list(payload.get("novel_insights", []))
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

    def write_run(self, output_dir: str | Path) -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "resolved_config.json").write_text(self.config.model_dump_json(indent=2), encoding="utf-8")
        (out / "saturation_trace.json").write_text(json.dumps(self.state.to_dict(), indent=2), encoding="utf-8")
        self.graph.write_graphml(out / "citation_graph.graphml")
        self.graph.render_dot(out / "growth_and_pruning.dot")
        self.graph.render_dot(out / "growth_and_pruning_study_family.dot", compressed_by_study_family=True)
        return out
