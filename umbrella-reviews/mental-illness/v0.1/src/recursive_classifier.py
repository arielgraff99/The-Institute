"""Minimal executable scaffold for the Mental Illness Umbrella Review.

This module intentionally does not assign biological ontology from a numerical score.
It validates the frozen historical ruler, enforces allowed output classes, and records
recursive nodes plus orthogonal axes for downstream evidence adjudication.
"""
from dataclasses import dataclass, asdict
from typing import List, Optional
import json

ALLOWED_CLASSES = {
    "DISTINCT_DISEASE",
    "BIOLOGICAL_SUBTYPE_OR_ENDOTYPE",
    "DIMENSION_OR_SPECTRUM",
    "DISEASE_STAGE",
    "TREATMENT_RESPONSE_STATE",
    "OPERATIONAL_CLINICAL_CATEGORY",
    "COMPOSITE_MULTIAXIAL",
    "INSUFFICIENT_EVIDENCE",
    "HETEROGENEOUS_RESIDUAL"
}

@dataclass
class ClassificationNode:
    node_id: str
    label: str
    parent_id: Optional[str]
    proposed_class: str
    status: str
    evidence_summary: str
    criteria_notes: str
    cross_cutting: bool = False
    children: Optional[List[str]] = None

    def validate(self):
        if self.proposed_class not in ALLOWED_CLASSES:
            raise ValueError(f"Unsupported class: {self.proposed_class}")
        if self.status not in {"SUPPORTED", "PARTIALLY_SUPPORTED", "PROVISIONAL", "NOT_SUPPORTED", "NOT_YET_TESTED"}:
            raise ValueError(f"Unsupported status: {self.status}")
        return self


def validate_framework(framework_path: str):
    with open(framework_path, encoding="utf-8") as f:
        fw = json.load(f)
    assert fw["framework_version"] == "0.2"
    assert fw["status"] == "FROZEN_FOR_DOWNSTREAM_TESTING"
    return fw


def export_nodes(nodes: List[ClassificationNode], out_path: str):
    payload = []
    for node in nodes:
        node.validate()
        payload.append(asdict(node))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
