# Historical Disease-Splitting Module

Purpose: derive reusable disease-division criteria from the history of medicine before applying them to any target disorder.

This module is intentionally target-independent. It should not know whether the downstream disease-specific review will concern depression, schizophrenia, Alzheimer disease, cancer, or another condition.

## Core logic

1. Identify historical conditions once treated as one disease or one broad diagnostic entity that were later divided into separate diseases, molecular/pathological subtypes, mechanistic endotypes, stages, or treatment-response states.
2. Identify failed, unstable, abandoned, or controversial proposed divisions as negative controls.
3. Reconstruct the chronology of each case rather than reading history backward from the current classification.
4. Reconstruct both the scientific evidence and the socioeconomic, political, technological, institutional, military, regulatory, commercial, and cultural context surrounding the division.
5. Ask separately: (a) why did the division occur at that historical moment? and (b) was the resulting division scientifically valid?
6. Use contextual factors as controls on historical inference. A war, recession, new technology, military need, research-funding shift, industrial incentive, or regulatory pathway may accelerate or delay recognition without determining the underlying biological validity.
7. Historical patterns may nominate candidate disease-splitting criteria, but they are promoted into the reusable framework only if they have face validity, cross-disease scientific coherence, measurable definitions, and some ability to distinguish successful from failed historical splits.
8. If a historical pattern lacks scientific coherence, report it as HISTORICAL_OBSERVATION_ONLY rather than forcing it into the criteria set.
9. Freeze the final criteria set before any disease-specific review uses it.

## Current status

Phase 1 reconnaissance started 2026-08-04. The first seed set deliberately spans different forms of classification:

- type 1 versus type 2 diabetes: etiologic/pathophysiological separation;
- Crohn disease versus ulcerative colitis: clinical-pathological separation;
- viral hepatitis A/B/non-A-non-B/C: etiologic separation with a major military/war context;
- acute promyelocytic leukemia within AML: distinctive clinicopathology, cytogenetics, molecular mechanism, and targeted treatment; important Chinese political-economic context;
- HER2-positive breast cancer: molecular/treatment-defined subtype enabled by molecular biology, biotechnology, public funding, industry development, diagnostics, and patient advocacy;
- asthma T2-high/T2-low: mechanistic endotype example rather than necessarily separate disease;
- relapsing/progressive multiple sclerosis: stage/phenotype comparator in which clinical-trial utility preceded objective biological separation;
- traditional schizophrenia subtypes: negative-control example removed because of poor stability, reliability, validity, longitudinal distinction, and treatment-response specificity.

No final disease-splitting criteria have been derived or frozen yet.

## Planned outputs

- historical_case_schema.json
- seed_cases.csv
- successful_split_matrix.csv
- failed_or_contested_split_matrix.csv
- contextual_attribution_matrix.csv
- candidate_criteria.csv
- criteria_face_validity_review.csv
- frozen_disease_splitting_framework.json
- methodology_report.md
- search_log.csv
- process_metrics.json
