# Codex Addendum: BPSD as a Cross-Dementia Clinical Phenotype Layer

## Scientific objective

Extend the brain-insulin-resistance dementia project so that behavioral and psychological symptoms of dementia (BPSD) are analyzed as a clinically meaningful phenotype dimension across and within dementia etiologies.

BPSD must not be represented as one binary variable, one total NPI score, or one immutable subtype. The implementation must retain symptom-level data, study-defined clusters, data-driven clusters, and longitudinal trajectories separately.

## Core question

Does a BPSD phenotype identify biologically distinct insulin-signaling states beyond what can be explained by dementia diagnosis, pathological substrate, genetic susceptibility, clinical stage, cognitive severity, systemic metabolic disease, medications, and environment?

## Clinical phenotype hierarchy

Represent clinical phenotype using at least these levels:

1. Dementia diagnosis/pathological substrate.
2. Cognitive phenotype and severity.
3. Functional phenotype.
4. BPSD individual symptoms.
5. BPSD syndrome/cluster phenotype.
6. BPSD longitudinal trajectory.
7. Treatment and environmental context.

Do not substitute one level for another.

## Symptom-level extraction

Capture at minimum when available:

- agitation
- aggression
- irritability
- delusions
- hallucinations
- apathy/withdrawal
- depression/dysphoria
- anxiety
- disinhibition
- impulsivity
- aberrant motor behavior/restlessness
- sleep/circadian disturbance
- REM sleep behavior disorder where relevant
- appetite/eating changes
- euphoria/elation
- rejection of care
- personality/behavioral change

Preserve severity, frequency, distress, duration, episodic versus persistent course, incident versus prevalent status, and instrument used.

## Cluster-level extraction

Record the exact cluster definition used by each study. Candidate recurring families may include:

- psychosis
- agitation/aggression/irritability
- apathy/withdrawal
- affective depression/anxiety
- disinhibition/impulsivity
- motor restlessness
- sleep/circadian
- appetite/eating
- mixed high-burden phenotype

These are search/normalization families only. Do not impose them on study data when the original factor structure differs.

## Longitudinal rule

BPSD can fluctuate, remit, recur, or change composition. Therefore:

- cross-sectional BPSD membership is not a fixed biological subtype;
- onset and trajectory must be represented separately;
- longitudinal analyses receive greater temporal weight than cross-sectional cluster analyses for causal ordering;
- earliest observed BPSD does not equal biological onset.

## Link to temporal insulin analysis

For each BPSD-insulin association determine, when possible:

INSULIN ABNORMALITY BEFORE BPSD

INSULIN ABNORMALITY CONCURRENT WITH BPSD

INSULIN ABNORMALITY AFTER BPSD

ORDERING UNRESOLVED

Also position both insulin and BPSD relative to:

- preclinical pathology
- prodromal/MCI stage
- dementia onset
- cognitive/functional decline
- neurodegeneration
- amyloid/tau/alpha-synuclein/TDP-43/vascular pathology

Do not infer precedence from disease severity correlations.

## Cross-dementia BPSD analysis

Analyze whether the same behavioral phenotype has the same biological correlate across:

- Alzheimer disease
- Lewy body dementia/Parkinson disease dementia
- frontotemporal dementia and genetic subtypes
- vascular cognitive impairment/dementia
- mixed dementias

The inverse analysis is also required: determine whether the same insulin-signaling phenotype expresses as different BPSD profiles depending on dementia substrate.

## Genetic integration

Cross BPSD phenotype with Model 0 genetics when data permit.

Examples of questions:

- Does APOE genotype modify an insulin-BPSD relationship in AD or mixed pathology?
- Do GBA1 or other Lewy-body/PD variants alter metabolic vulnerability associated with hallucinations, fluctuation, apathy, or sleep behavior?
- Do GRN, MAPT, or C9orf72 define distinct metabolic-behavioral phenotypes in FTD?
- Are metabolic polygenic-risk scores associated with BPSD independently of cognitive decline?

These are hypotheses to test, not assumptions.

## Healthy-aging and adaptive-aging control

Include healthy older adults and, where available, exceptional-aging cohorts to distinguish:

- normal age-associated behavioral variation
- adaptive insulin-signaling changes
- dementia-specific behavioral-metabolic phenotypes

A BPSD-insulin association must not be labeled pathological solely because both variables differ from young controls.

## Confounding and reverse-causation audit

Explicitly audit:

- delirium
- acute infection/medical illness
- pain
- sensory impairment
- sleep disruption
- psychotropic medication exposure
- antipsychotics
- antidepressants
- sedatives/hypnotics
- cholinesterase inhibitors/memantine
- dopaminergic drugs
- systemic diabetes and insulin resistance
- obesity and nutritional state
- vascular burden
- frailty
- institutionalization/care environment
- caregiver/environmental triggers

Medication exposure requires special treatment because BPSD can cause medication use and medication can alter metabolic state, producing bidirectional confounding.

## Required modeling comparisons

Where data permit compare models using nested prediction/association structures:

A. Dementia diagnosis alone.

B. Diagnosis + cognitive stage.

C. Diagnosis + pathology.

D. Diagnosis + BPSD phenotype.

E. Pathology + BPSD.

F. Genetics + BPSD.

G. Insulin phenotype + BPSD.

H. Integrated multiaxial model: genetics + pathology + insulin phenotype + cognition + BPSD + vascular/systemic context.

Do not interpret improved prediction as proof of causal mechanism.

## Required outputs

Create:

- `bpsd_symptom_level_evidence_matrix.csv`
- `bpsd_cluster_definitions.csv`
- `bpsd_longitudinal_trajectory_ledger.csv`
- `insulin_bpsd_cross_dementia_matrix.csv`
- `bpsd_confounder_medication_audit.csv`
- `bpsd_pathology_genotype_interaction_matrix.csv`
- `bpsd_clinical_subtype_report.md`

The final scientific report must answer:

1. Are there reproducible BPSD phenotypes associated with brain insulin-signaling abnormalities?
2. Are those associations independent of dementia etiology and severity?
3. Are they shared across dementias or disease-specific?
4. Do insulin abnormalities precede particular BPSD trajectories?
5. Do genetic and pathological substrates modify the relationship?
6. Could the apparent association be medication-, systemic-metabolic-, vascular-, environmental-, or severity-driven?
7. Does BPSD phenotyping improve mechanistic discrimination beyond the conventional dementia diagnosis?

## Interpretation requirement

The project should ultimately support a multiaxial representation rather than force a single subtype label:

GENETIC SUSCEPTIBILITY
+
PATHOLOGICAL SUBSTRATE
+
INSULIN/METABOLIC PHENOTYPE
+
COGNITIVE/FUNCTIONAL STAGE
+
BPSD PHENOTYPE/TRAJECTORY
+
SYSTEMIC AND ENVIRONMENTAL CONTEXT

This representation permits the same pathological dementia to have different metabolic-behavioral phenotypes and permits similar BPSD syndromes to arise through different mechanisms.