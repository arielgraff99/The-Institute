from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class RiskOfBiasResult:
    study_id: str
    result_id: str
    design: str
    tool: str
    domain_judgments: dict[str, str] = field(default_factory=dict)
    overall_judgment: str = "unclear"
    rationale: tuple[str, ...] = ()


DEFAULT_ROB_ROUTING: dict[str, str] = {
    "randomized_trial": "RoB 2",
    "nonrandomized_intervention": "ROBINS-I",
    "diagnostic_accuracy": "QUADAS-2",
    "prediction_model": "PROBAST_or_successor",
    "systematic_review": "ROBIS_AMSTAR2",
    "meta_analysis": "ROB-ME_plus_review_appraisal",
    "qualitative": "CASP_or_JBI",
    "mixed_methods": "MMAT",
    "animal": "SYRCLE",
    "observational": "JBI_or_domain_specific",
    "basic_science": "domain_specific_basic_science",
    "omics": "domain_specific_omics",
}


def route_risk_of_bias_tool(design: str, overrides: dict[str, str] | None = None) -> str:
    key = design.strip().casefold().replace(" ", "_")
    routing = dict(DEFAULT_ROB_ROUTING)
    if overrides:
        routing.update({str(k).casefold(): str(v) for k, v in overrides.items()})
    return routing.get(key, "manual_appraisal_required")


def validate_result_level_appraisal(results: Iterable[RiskOfBiasResult]) -> list[str]:
    """Return audit errors. A publication-level blanket score is not enough."""
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    for item in results:
        key = (item.study_id, item.result_id)
        if key in seen:
            errors.append(f"duplicate_result_appraisal:{item.study_id}:{item.result_id}")
        seen.add(key)
        if not item.result_id.strip():
            errors.append(f"missing_result_id:{item.study_id}")
        if item.overall_judgment not in {"low", "some_concerns", "high", "unclear", "not_applicable"}:
            errors.append(f"invalid_overall_judgment:{item.study_id}:{item.result_id}")
    return errors
