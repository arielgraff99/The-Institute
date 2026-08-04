from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RegistryRecord:
    registry_id: str
    status: str
    primary_outcomes: tuple[str, ...] = ()
    secondary_outcomes: tuple[str, ...] = ()
    planned_sample_size: int | None = None
    completion_date: str | None = None


@dataclass(frozen=True)
class PublicationRecord:
    publication_id: str
    registry_id: str | None = None
    reported_outcomes: tuple[str, ...] = ()
    analyzed_sample_size: int | None = None
    publication_date: str | None = None


def compare_registration(registry: RegistryRecord, publication: PublicationRecord) -> dict[str, object]:
    planned = {x.casefold().strip() for x in registry.primary_outcomes + registry.secondary_outcomes if x.strip()}
    reported = {x.casefold().strip() for x in publication.reported_outcomes if x.strip()}
    missing = sorted(planned - reported)
    added = sorted(reported - planned)
    sample_delta = None
    if registry.planned_sample_size is not None and publication.analyzed_sample_size is not None:
        sample_delta = publication.analyzed_sample_size - registry.planned_sample_size
    return {
        "registry_id": registry.registry_id,
        "publication_id": publication.publication_id,
        "missing_registered_outcomes": missing,
        "unregistered_reported_outcomes": added,
        "sample_size_delta": sample_delta,
        "completed_without_publication": False,
    }


def completed_without_publication(registry: RegistryRecord, matched_publications: list[PublicationRecord]) -> bool:
    completed = registry.status.casefold() in {"completed", "terminated", "stopped"}
    return completed and len(matched_publications) == 0
