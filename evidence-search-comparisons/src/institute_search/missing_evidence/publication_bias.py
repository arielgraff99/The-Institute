from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MissingEvidenceSignal:
    signal_type: str
    source_id: str
    description: str
    material: bool = True
    confidence: str = "unclear"
    provenance: tuple[str, ...] = field(default_factory=tuple)


@dataclass
class PublicationBiasAudit:
    signals: list[MissingEvidenceSignal] = field(default_factory=list)
    funnel_test_p_value: float | None = None
    fail_safe_n: float | None = None

    @property
    def concern_level(self) -> str:
        material = [s for s in self.signals if s.material]
        if any(s.signal_type in {"registered_outcome_missing", "completed_unpublished", "selective_reporting"} for s in material):
            return "high"
        if material:
            return "some_concern"
        return "unresolved"

    def interpret_funnel_test(self) -> str:
        if self.funnel_test_p_value is None:
            return "not_assessed"
        if self.funnel_test_p_value < 0.05:
            return "asymmetry_signal_requires_investigation"
        return "no_detected_asymmetry_does_not_exclude_publication_bias"

    def fail_safe_n_is_primary_evidence(self) -> bool:
        return False


def signal_is_novel_insight(signal: MissingEvidenceSignal) -> bool:
    return bool(signal.material and signal.provenance and signal.description.strip())
