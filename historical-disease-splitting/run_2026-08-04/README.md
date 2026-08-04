# Historical Disease-Splitting Run — 2026-08-04

This directory contains the first completed run of the standalone historical module.

## Inputs

The module was intentionally target-independent. No depression, schizophrenia, or other downstream target disorder was allowed to define the criteria.

## Evidence set

- 21 historical comparators
- 16 accepted or operationally accepted classifications/reclassifications
- 5 failed, merged, contested, or over-subtyped controls
- multiple division classes represented: distinct disease, molecular subtype, mechanistic endotype, stage/phenotype, treatment-response state, operational category

## Files

- `historical_case_matrix.csv` — 21-case scientific reconstruction
- `contextual_attribution_matrix.csv` — socioeconomic, political, military, technological, institutional, commercial, regulatory and measurement controls
- `candidate_criteria_face_validity.csv` — candidate criteria and promotion decisions
- `frozen_disease_splitting_framework_v0.1.json` — versioned one-way output to disease-specific review modules
- `methodology_report.md` — synthesis and interpretation
- `search_log.csv` — exact queries retained after log normalization
- `process_metrics.json` — coverage, telemetry and malfunction metadata

## Primary methodological result

The historical evidence does not support one class-agnostic disease-splitting score. It supports:

1. universal validity requirements;
2. class-specific gates for distinct disease, subtype/endotype, stage, treatment-response state and operational category;
3. a separate historical-context control layer.

Historical adoption factors such as war, economic conditions, funding, technology, authority, regulation and commercial opportunity can nominate explanations for when a split appeared or persisted, but they are not themselves intrinsic evidence that two diseases exist.

## Freeze rule

Framework v0.1 is frozen for testing. Historical expansion must create v0.2 or later. A disease-specific module can propose an amendment but cannot directly modify v0.1.
