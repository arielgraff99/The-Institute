from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class CycleAudit:
    cycle_id: str
    generation_number: int
    novel_insights: list[dict[str, Any]] = field(default_factory=list)
    new_records_count: int = 0
    new_study_families_count: int = 0
    pruned_nodes_count: int = 0
    tokens: int | None = None
    cost: float | None = None

    @property
    def zero_novel_insight(self) -> bool:
        return len(self.novel_insights) == 0


@dataclass
class RunState:
    run_id: str
    project_id: str
    cycles: list[CycleAudit] = field(default_factory=list)
    consecutive_zero_novel_insight_cycles: int = 0
    status: str = "INITIALIZED"
    metadata: dict[str, Any] = field(default_factory=dict)

    def register_cycle(self, audit: CycleAudit) -> None:
        self.cycles.append(audit)
        if audit.zero_novel_insight:
            self.consecutive_zero_novel_insight_cycles += 1
        else:
            self.consecutive_zero_novel_insight_cycles = 0

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["cycles"] = [asdict(c) | {"zero_novel_insight": c.zero_novel_insight} for c in self.cycles]
        return data
