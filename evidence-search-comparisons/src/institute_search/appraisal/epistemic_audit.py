from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class EpistemicAudit:
    claim_id: str
    directness: str
    risk_of_bias: str
    replication_count: int
    missing_evidence_concern: str
    measurement_validity: str = "unassessed"
    temporality: str = "unassessed"
    notes: tuple[str, ...] = field(default_factory=tuple)

    def dimensions(self) -> dict[str, object]:
        """Keep dimensions separate; do not collapse to a single quality score."""
        return {
            "directness": self.directness,
            "risk_of_bias": self.risk_of_bias,
            "replication_count": self.replication_count,
            "missing_evidence_concern": self.missing_evidence_concern,
            "measurement_validity": self.measurement_validity,
            "temporality": self.temporality,
            "notes": list(self.notes),
        }
