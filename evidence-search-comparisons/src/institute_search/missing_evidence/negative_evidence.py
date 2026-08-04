from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NegativeEvidenceRecord:
    source_id: str
    study_family_id: str
    finding_type: str
    claim_id: str
    summary: str
    material: bool = True
    provenance: tuple[str, ...] = ()

    @property
    def qualifies_as_novel_insight(self) -> bool:
        return bool(self.material and self.summary.strip() and self.provenance)


ALLOWED_NEGATIVE_TYPES = {
    "null",
    "contradictory",
    "failed_replication",
    "completed_unpublished",
    "missing_registered_outcome",
    "negative_preclinical",
    "negative_clinical",
}


def validate_negative_record(record: NegativeEvidenceRecord) -> list[str]:
    errors: list[str] = []
    if record.finding_type not in ALLOWED_NEGATIVE_TYPES:
        errors.append(f"unsupported_negative_evidence_type:{record.finding_type}")
    if not record.provenance:
        errors.append(f"missing_provenance:{record.source_id}")
    return errors
