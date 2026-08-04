# Historical Disease-Splitting Module — v0.2 Stress Test

Run date: 2026-08-04
Base framework: v0.1
Output framework: `frozen_disease_splitting_framework_v0.2.json`

## Purpose

v0.2 is a prospective stress test of the frozen v0.1 framework. It does not simply add favorable examples. New comparators were selected to challenge v0.1 using:

- diseases separated from a prior umbrella by new antibodies or molecular assays;
- molecular subtypes with treatment interactions;
- accepted biological spectra without categorical boundaries;
- treatment/stage/operational classifications;
- residual categories defined mainly by absence of another marker;
- classifications later merged or revised;
- country/geography-based classifications later superseded by biology;
- low- and middle-income-country conditions with historical research neglect;
- classifications strongly affected by technology, regulation, consensus or health-system context.

## Evidence set

- v0.1 comparators inherited: 21
- new v0.2 comparators: 19
- total comparators: 40
- accepted, operationally accepted, or emerging-with-substantial-support: 28
- failed, merged, contested, residual, or materially revised controls: 12

The 19 additions include NMOSD, MOGAD, MODY, Burkitt lymphoma, historical Burkitt epidemiologic subtypes, the Ridley-Jopling leprosy spectrum, rheumatoid-arthritis serotypes, sepsis definitions, heart-failure EF phenotypes, papillary-RCC type 1/2, narcolepsy type 1/2, driver-defined NSCLC, prion-disease etiologic forms, the Kraepelinian psychosis boundary, low- versus high-grade serous ovarian carcinoma, ANCA-associated vasculitis classifications, axial-spondyloarthritis stages/spectrum, IBS stool-pattern subtypes, and malnutrition-related/type 5 diabetes.

## Primary v0.2 changes

v0.1 was substantially preserved. The expanded history justified the following amendments:

1. Add `DIMENSION_OR_SPECTRUM` as a legitimate classification outcome. A coherent biological continuum must not be forced into artificial diseases.
2. Add `U08_CONVERGENT_MULTI_DOMAIN_COHERENCE` for claims of biological ontology. Strong disease/endotype claims should generally converge across independent domains unless one causal discriminator is exceptionally specific.
3. Add `U09_POSITIVE_DEFINITION_RESIDUAL_CAUTION`. A residual group defined mainly as "not subgroup A" is provisional unless positive reproducible coherence is demonstrated.
4. Add a `COMPOSITE_MULTIAXIAL` rule. A condition may simultaneously have an etiologic subtype, stage, treatment-response state and dimensional severity axis.
5. Add `H07_RESEARCH_OPPORTUNITY_ASYMMETRY`. Lack or delay of evidence is interpreted cautiously when populations lack diagnostic technology, surveillance, funding or commercial attention.
6. Add `H08_JURISDICTIONAL_ADOPTION_DIVERGENCE`. Country-specific or regulator-specific classification decisions are recorded separately from scientific validity.
7. Add a target-family holdout sensitivity rule: when the downstream target is closely related to a historical comparator used in criteria derivation, repeat adjudication excluding that comparator/family to test for criterion leakage.

## What did not change

The core v0.1 findings survived:

- no single class-agnostic disease-splitting score;
- universal validity requirements plus classification-specific gates;
- treatment response alone is not disease ontology;
- regulatory/expert adoption is not biological proof;
- historical timing is strongly context-dependent;
- stages require longitudinal ordering rather than immutable membership;
- resistance states require adequate exposure and pseudoresistance assessment;
- operational categories can be clinically valid without being separate diseases.

## Files

- `added_cases_v0.2.csv`
- `historical_case_matrix_v0.2.csv`
- `v0.1_to_v0.2_amendment_analysis.md`
- `frozen_disease_splitting_framework_v0.2.json`
- `methodology_report_v0.2.md`
- `search_log_v0.2.csv`
- `process_metrics_v0.2.json`

## Freeze rule

v0.2 is frozen for downstream testing after this run. Any further historical change must create v0.3 or later. Disease-specific modules may propose amendments but cannot edit a frozen historical framework.