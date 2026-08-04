from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class Insight:
    category: str
    summary: str
    provenance: list[str]
    material: bool = True


class NoveltyHook(Protocol):
    def evaluate(self, cycle_payload: dict[str, Any]) -> list[Insight]: ...


DEFAULT_NON_NOVEL = {
    "duplicate_publication",
    "review_restatement",
    "paraphrase",
    "llm_agreement_only",
    "bibliographic_only",
}


def normalize_insights(raw: list[dict[str, Any]]) -> list[Insight]:
    out: list[Insight] = []
    seen: set[tuple[str, str]] = set()
    for item in raw:
        category = str(item.get("category", "")).strip()
        summary = str(item.get("summary", "")).strip()
        if not category or not summary or category in DEFAULT_NON_NOVEL:
            continue
        if item.get("material", True) is False:
            continue
        provenance = [str(x) for x in item.get("provenance", []) if str(x).strip()]
        if not provenance:
            continue
        key = (category, summary.casefold())
        if key in seen:
            continue
        seen.add(key)
        out.append(Insight(category, summary, provenance, True))
    return out
