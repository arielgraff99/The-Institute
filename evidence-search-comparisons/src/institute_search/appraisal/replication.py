from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvidenceUnit:
    publication_id: str
    study_family_id: str
    cohort_id: str | None = None
    dataset_id: str | None = None
    laboratory_id: str | None = None
    pipeline_id: str | None = None


def independent_replication_count(units: Iterable[EvidenceUnit]) -> int:
    """Count independent study families, never publications or LLM agreement."""
    families = {u.study_family_id for u in units if u.study_family_id.strip()}
    return len(families)


def publication_count(units: Iterable[EvidenceUnit]) -> int:
    return len({u.publication_id for u in units if u.publication_id.strip()})
