# Historical Disease-Splitting Reconstruction Prompt

You are executing the historical module of a disease-classification research system. Your task is to reconstruct how medicine has historically divided broad disease concepts into separate diseases, biological subtypes, mechanistic endotypes, stages, treatment-response states, or operational categories, and to identify failed or abandoned splits as negative controls.

Do not analyze any downstream target disorder. This module must remain target-independent.

## For each historical case

Reconstruct the chronology without reading present knowledge backward into the past.

Identify:

1. the original unified disease concept;
2. the first observations suggesting heterogeneity;
3. the date/era and country/institution of those observations;
4. the clinical, pathological, epidemiological, physiological, molecular, genetic, treatment-response or other evidence that accumulated;
5. what evidence existed before formal subdivision;
6. what evidence appeared only after subdivision;
7. whether treatment differences preceded mechanistic understanding;
8. whether molecular understanding preceded treatment differentiation;
9. whether subgroup membership was stable, transitional, overlapping or uncertain;
10. whether independent cohorts/regions/laboratories reproduced the distinction;
11. whether the subdivision improved diagnosis, prognosis, treatment, prevention, trial design, or other clinical decisions;
12. whether diagnostic systems, specialty societies or regulators formally adopted the distinction;
13. whether the distinction persisted, changed, merged, or was abandoned.

## Historical-context reconstruction

Build a parallel context timeline including, where relevant:

- national and global economic conditions;
- war, occupation, civil conflict or political instability;
- government and military priorities;
- public-health priorities;
- research funding;
- technology availability and cost;
- specialist and laboratory infrastructure;
- health-system organization;
- international scientific exchange;
- commercial and pharmaceutical incentives;
- patents and diagnostic markets;
- regulatory incentives;
- reimbursement;
- patient advocacy;
- social and cultural forces.

Do not assume that adverse context always slows research. A war, epidemic, military deployment or political program may redirect resources and accelerate work in a strategically important disease.

## Separate two causal questions

Always distinguish:

A. Why was this disease division recognized or adopted at this historical moment?

B. Was the resulting disease division scientifically valid?

Never infer biological validity solely from adoption, persistence, regulatory recognition, economic investment, or historical prestige.

Never infer lack of heterogeneity solely from delayed recognition.

## Counterfactual historical test

Ask:

If the later technology, funding, infrastructure and political stability had existed earlier, would the distinction plausibly have been detectable earlier?

Label the answer LIKELY, POSSIBLE, UNLIKELY or UNKNOWN and clearly mark it as inference.

## Context attribution

Classify historical timing/adoption as one of:

CONTEXT_DOMINANT
CONTEXT_MAJOR
MIXED
SCIENCE_MAJOR
SCIENCE_DOMINANT
INDETERMINATE

Classify the scientific outcome separately as:

BIOLOGICAL_SPLIT_VALIDATED
CLINICALLY_USEFUL_SPLIT
TEMPORARY_OR_FAILED_SPLIT
ONTOLOGY_UNRESOLVED

Do not assign numerical percentages unless the historical evidence genuinely supports quantitative attribution.

## Candidate-criterion nomination

Historical cases may nominate possible reusable disease-splitting criteria, but do not promote them automatically.

For every candidate criterion ask:

- Does it have face validity?
- Is there a coherent relationship to disease mechanism, natural history, prognosis, treatment, or stable phenotype?
- Can it be defined and measured across different disorders?
- Does it help distinguish successful historical splits from failed splits?
- Is it robust to socioeconomic, political, technological and institutional context?
- Could it be prospectively applied to a new disease without circular reasoning?

Candidate criteria that fail this test must be retained only as:

HISTORICAL_OBSERVATION_ONLY

or

CONTEXTUAL_HISTORICAL_FACTOR

Do not invent scientific coherence to rescue a weak historical pattern.

## Evidence discipline

Prefer primary historical papers, authoritative historical reviews, institutional histories, regulatory records and contemporaneous documents.

Distinguish direct historical evidence from retrospective interpretation.

Do not count multiple publications from one parent cohort/trial as independent replication.

Search for contradictory accounts and later reassessments.

## Output

For every case produce:

- completed historical-case record;
- scientific timeline;
- context timeline;
- contextual attribution;
- scientific-validity outcome;
- unresolved uncertainties;
- candidate criterion nominations;
- source provenance.

At the end of a batch, compare successful and failed cases but do not freeze criteria until the sample is sufficiently diverse across specialties, countries, eras, technologies and contextual conditions.
