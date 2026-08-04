# Evidence Search Prompt Comparisons

Backup of the prompt and research-pipeline comparison work developed in ChatGPT during July-August 2026.

The purpose of this directory is to preserve distinct experimental runs rather than overwrite earlier outputs with later revisions. Conclusions and methods should therefore be interpreted according to the provenance and verification status below.

## Run families

### 2026-07-31: Simulated Co-Scientist versus Evidence-Grounded Clinical Model

Directory: `2026-07-31_cosci-vs-clinical/`

Files:

- `Report_1_Simulated_AI_CoScientist.md` — simulation of a Generation/Proximity/Reflection/Ranking/Evolution/Meta-review research architecture applied to delusion versus confabulation.
- `Report_2_Evidence_Grounded_Clinical_Model.md` — alternative pipeline emphasizing clinical discrimination, explicit alternatives, evidence traceability, and avoiding forced model ranking.
- `Report_3_Process_Metrics_and_Costs.md` — direct process comparison plus illustrative token and API-cost scenarios.

Status: methodological comparison. The Co-Scientist run was a transparent simulation and did not access Google's proprietary Co-Scientist service.

### 2026-08-01: Baseline MDD versus TRD entity test

Directory: `2026-08-01_mdd-trd-baseline/`

File:

- `03_Depression_Entity_Test.md` — baseline multi-domain assessment of whether treatment-resistant depression is a distinct disease, a stage/severity state, multiple endotypes, an operational category, or a mixed model.

Status: baseline evidence-map run. Useful as the comparison condition for the later integrity-integrated rerun.

### 2026-08-03: Integrity-integrated MDD/TRD rerun

Directory: `2026-08-03_integrity-rerun/`

File:

- `comparison_revised_run.md` — controlled rerun preserving the original question and competing models while adding study-family linkage, result-level appraisal, registry/missing-evidence surveillance, explicit claim blocking, and dynamic search redistribution.

Status: later and more conservative methodological iteration. It does not reverse the baseline conclusion but changes the strength and wording of several claims.

## Reusable prompts

Directory: `prompts/`

- `Deep_Search_with_Classification_Prompt.md` — earlier reusable recursive evidence-search prompt.
- `master_orchestration_prompt.md` — orchestration prompt for the integrity-integrated multi-agent/search-role architecture.

## Configurations and telemetry

Directory: `config/`

- `institute_search_config.json` — MDD/TRD-specific configuration used for the Institute Evidence Integrity Search pilot.
- `process_metrics_template.json` — event-, cycle-, role-, token-, cost-, failure-, retry-, and malfunction-metadata schema for future executions.

## Canonical domain-agnostic specification

A File Library artifact named `domain_agnostic_multiagent_search.json`, specification version 2.0.0, was developed on 2026-08-03 as the provider-neutral portable specification underlying the later architecture. It includes model validation, independent functional roles, evidence ledgers, claim blocking, recursive citation expansion, saturation rules, citation-graph outputs, token telemetry, and an execution algorithm.

It is intentionally **not reconstructed from truncated excerpts in this GitHub backup**. The exact source artifact should be copied verbatim when direct full-file transfer is available. Reconstructing a long JSON specification from partial retrieval would risk silently changing the protocol.

## Legacy/unverified output

An earlier artifact, `metafile (1).md`, was identified from the comparison history. It contains stronger claims and search/database assertions that the later integrity workflow specifically treats as requiring verification. It has therefore not been promoted into the canonical evidence files. If archived later, it should be stored under `legacy_unverified/` with its original text and provenance intact.

## Interpretation rule

Do not treat agreement between runs or agents as independent scientific replication. Evidence independence is determined by underlying study families, cohorts, datasets, laboratories, and analytic pipelines. Preserve earlier runs for methodological comparison, but use the later integrity framework for claims requiring evidentiary adjudication.

## Backup date

Repository backup assembled on 2026-08-04 in `arielgraff99/The-Institute`.
