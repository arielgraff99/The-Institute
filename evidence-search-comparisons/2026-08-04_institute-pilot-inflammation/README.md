# Institute Configuration Pilot: Pretreatment Inflammation and Future Antidepressant Resistance

Run date: 2026-08-04

Configuration: `evidence-search-comparisons/config/institute_search_config.json`

Orchestration: `evidence-search-comparisons/prompts/master_orchestration_prompt.md`

## Frozen pilot question

Does pretreatment peripheral inflammation prospectively identify patients who will develop antidepressant resistance, beyond depression severity and major confounders?

This narrow branch was selected as a stress test of the Institute configuration because it directly tests temporality, specificity, replication, study-family independence, treatment interaction, missing evidence, and claim blocking.

## Competing models retained

- H1: Distinct disease
- H2: Stage or severity
- H3: Multiple endotypes
- H4: Operational treatment-course category
- H5: Mixed model
- H0: Artefact or selection model

No model was removed before searching.

## Execution limitation

The ChatGPT environment did not provide multiple genuinely independent model instances. Functional roles were therefore executed sequentially as isolated analytic passes, as permitted by the master orchestration prompt. Agreement among passes was not counted as independent evidence.

Web-accessible sources only were used. This is a pilot evidence map, not an exhaustive systematic review. Exact database result counts are not reported because the search interface did not provide reproducible source-level counts, consistent with claim-block rule CB8.

## Main pilot finding

Inflammation currently fits better as a candidate treatment-modifying endotype that may cut across MDD and TRD than as evidence that TRD itself is one separate inflammatory disease.

Evidence that supports this formulation includes pretreatment CRP or cytokine associations with differential treatment response in GENDEP, CO-MED, EMBARC, and anti-inflammatory treatment trials. However, the central ontology claim remains unproven because:

1. Most studies measure inflammation after prior illness and treatment exposure, not before resistance develops.
2. Associations are sensitive to BMI, smoking, metabolic disease, symptom pattern, sex, and other confounders.
3. Large study families produce multiple publications that must not be counted as independent replication.
4. Inflammatory thresholds vary substantially.
5. Cross-sectional TRD-versus-responsive comparisons cannot establish that inflammation preceded resistance.
6. No identified study prospectively followed a treatment-naive first-episode cohort through at least two adequate antidepressant failures and independently validated an inflammatory classifier of future TRD.

## Integrity finding from the 2026 meta-analysis

The 2026 Cureus meta-analysis by Hummad et al. reported a pooled OR of 2.11 for antidepressant nonresponse with elevated baseline inflammatory markers and low heterogeneity. The Institute audit does not accept that pooled estimate as independent confirmation of a TRD disease boundary without reanalysis because its included-study table contains multiple publications from the same GENDEP parent cohort, includes cross-sectional/retrospective TRD evidence, uses heterogeneous biomarker thresholds, and includes an infliximab TRD treatment study alongside conventional antidepressant prediction studies. Its protocol was developed a priori but was not prospectively registered in PROSPERO. These issues trigger study-family deduplication and downgrade/claim-block rules.

## Current model ranking for this branch

1. H5 Mixed model: best fit
2. H3 Multiple endotypes: strongest biologically informative component
3. H4 Operational treatment-course category: strongly supported
4. H2 Stage or severity: plausible and partly supported
5. H0 Artefact or selection: substantial contribution remains plausible
6. H1 Distinct disease: not demonstrated by this branch

The ranking is qualitative and does not represent numerical model probabilities.

## Required pilot deliverables

All nine deliverables specified by the Institute configuration are present:

- `search_log.csv` — exact search queries executed in this chat pilot; result counts intentionally omitted when not reproducibly exposed
- `reference_master.csv` — shared evidence ledger with study-family identity, design, outcomes, bias and model relation
- `study_family_map.csv` — parent cohorts/trials and companion publications to prevent false replication
- `claim_evidence_matrix.csv` — central claims, evidence labels, blockers and required verification
- `risk_of_bias.csv` — result-level pilot bias screen; explicitly not represented as a completed formal RoB/ROBINS assessment
- `missing_evidence_log.csv` — registry/protocol/publication matching and unresolved missing-evidence questions
- `audit_log.csv` — epistemic-auditor decisions and claim-block events
- `model_comparison.md` — claim-level synthesis and model adjudication
- `process_metrics.json` — execution telemetry, 38 exact queries, unavailable token/cost fields left null, and tool-failure metadata

## Decisive next study

A strong discriminator would enroll treatment-naive first-episode MDD, measure hs-CRP/IL-6 repeatedly before treatment, control medical/metabolic and socioeconomic confounding, verify drug exposure/adherence, apply prospectively standardized adequate treatment sequences, and determine whether a prespecified inflammatory classifier predicts failure of at least two mechanistically adequate treatments. A subsequent biomarker-stratified randomized trial would then need to show treatment-by-biomarker interaction and improved clinical decision utility.
