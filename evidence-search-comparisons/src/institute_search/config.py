from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, model_validator


class SaturationConfig(BaseModel):
    minimum_consecutive_zero_novel_insight_cycles: int = 3
    minimum_recursive_generations: int = 3
    soft_generation_review_point: int = 12
    never_label_resource_exhaustion_as_saturation: bool = True

    @model_validator(mode="after")
    def validate_saturation(self) -> "SaturationConfig":
        if self.minimum_consecutive_zero_novel_insight_cycles < 3:
            raise ValueError("Saturation requires at least 3 consecutive zero-insight cycles")
        if self.minimum_recursive_generations < 1:
            raise ValueError("minimum_recursive_generations must be >= 1")
        return self


class VisualizationConfig(BaseModel):
    enabled: bool = True
    canonical_structure: str = "directed_graph"
    human_projection: str = "left_to_right_dendrogram_like_growth_and_pruning_map"
    record_level: bool = True
    study_family_compressed: bool = True


class RunConfig(BaseModel):
    project_id: str
    project_title: str = ""
    research_question: str
    scientific_models: list[dict[str, Any]] = Field(default_factory=list)
    saturation: SaturationConfig = Field(default_factory=SaturationConfig)
    visualization: VisualizationConfig = Field(default_factory=VisualizationConfig)
    novelty_categories: list[str] = Field(default_factory=list)
    required_outputs: list[str] = Field(default_factory=list)
    extensions: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_models(self) -> "RunConfig":
        if len(self.scientific_models) < 3:
            raise ValueError("At least 3 genuinely competing scientific models are required")
        ids = [str(m.get("id", "")) for m in self.scientific_models]
        if len(ids) != len(set(ids)):
            raise ValueError("Scientific model IDs must be unique")
        return self


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _deep_merge(out[key], value)
        else:
            out[key] = value
    return out


def load_config(path: str | Path, *overlays: str | Path) -> RunConfig:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    for overlay in overlays:
        payload = _deep_merge(payload, json.loads(Path(overlay).read_text(encoding="utf-8")))

    if "recursive_generation" in payload and "saturation" not in payload:
        rg = payload["recursive_generation"]
        payload["saturation"] = {
            "minimum_consecutive_zero_novel_insight_cycles": rg.get(
                "minimum_consecutive_zero_novel_insight_cycles_for_saturation", 3
            ),
            "minimum_recursive_generations": rg.get("minimum_recursive_generations", 3),
            "soft_generation_review_point": payload.get("resource_guard", {}).get(
                "soft_generation_review_point", 12
            ),
            "never_label_resource_exhaustion_as_saturation": payload.get("resource_guard", {}).get(
                "never_label_resource_exhaustion_as_saturation", True
            ),
        }

    return RunConfig.model_validate(payload)
