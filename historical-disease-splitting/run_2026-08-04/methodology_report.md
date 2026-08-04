# Historical Disease-Splitting Module — First Full Run

Run date: 2026-08-04
Framework output: `frozen_disease_splitting_framework_v0.1.json`

## Question

Across the history of medicine, what evidence has allowed an apparently unitary illness or diagnostic category to be divided into distinct diseases, biological subtypes/endotypes, disease stages, or treatment-response states, and which apparent divisions subsequently failed? How much of the timing and adoption of those divisions is explained by scientific evidence versus socioeconomic, political, technological, institutional, military, commercial, regulatory, or cultural context?

## Scope

This first full run used a purposive historical evidence map rather than claiming exhaustive coverage of all medical reclassification. Twenty-one comparators were reconstructed across endocrinology, gastroenterology, infectious disease, oncology/hematology, respiratory medicine, neurology, psychiatry and developmental disorders.

Sixteen cases represent accepted or operationally accepted divisions/reclassifications and five are failed, merged, contested or over-subtyped controls.

The sample deliberately contains different ontological classes:

- distinct etiologic diseases;
- molecular/pathological subtypes;
- mechanistic endotypes;
- longitudinal disease stages/phenotypes;
- treatment-response states;
- operational clinical categories;
- failed or abandoned categories.

## Main findings

### 1. A single universal disease-splitting score is historically incoherent

The evidence needed to establish two distinct diseases is not identical to the evidence needed to establish a disease stage or treatment-response state.

For example, viral hepatitis and HIV-1/HIV-2 became compelling distinct-disease cases after distinct causal agents were demonstrated. In contrast, multiple-sclerosis course phenotypes were explicitly created as useful clinical/trial descriptors despite absence of objective biological separators. Drug-resistant epilepsy was intentionally defined as a testable treatment-response construct after adequate treatment failures rather than as a separate disease.

Therefore the framework uses universal validity requirements plus classification-specific gates.

### 2. Molecular understanding does not need to precede a valid division

Crohn disease was recognized clinicopathologically before contemporary molecular mechanisms. APL was recognized by morphology/coagulopathy, and ATRA differentiation therapy was effective before the PML::RARA mechanism was fully known. Conversely, later mechanistic confirmation greatly strengthened these classifications.

The historical module therefore rejects a rule requiring molecular evidence before subdivision. Molecular/etiologic evidence is strongest for claims of distinct disease or mechanistic endotype but is not universally required for stages or operational categories.

### 3. Technology is an opportunity variable, not proof

Technology enabled both successful and unsuccessful distinctions.

- improved chromosome visualization revealed the Philadelphia chromosome and ultimately BCR::ABL1 CML;
- molecular pathology and KIT biology clarified GIST;
- serology/molecular virology distinguished viral hepatitides;
- renin assays generated the low-renin hypertension hypothesis, but assay/population/sodium dependence undermined the idea of one clean separate low-renin disease.

Thus availability of a biomarker or new technology cannot itself validate a category.

### 4. Historical context can strongly change timing without changing biological truth

Two cases are particularly informative natural experiments.

**Viral hepatitis:** World War II outbreaks and yellow-fever-vaccine-associated hepatitis created direct military urgency. Military investigations helped distinguish infectious from serum hepatitis before the causal viruses were identified. War accelerated discovery.

**APL:** arsenic and retinoic-acid discoveries in China occurred under severe Cultural Revolution disruption. Historical accounts describe suppression of scientific careers and delayed international recognition; later China–France collaboration accelerated reproduction and adoption. Political disruption delayed or obscured discovery, while the biological result remained valid.

The framework therefore prohibits interpreting time-to-recognition as a measure of biological distinctness without contextual adjustment.

### 5. Context can also preserve weak classifications

The presenile Alzheimer disease versus senile dementia split is a strong negative control. Historical analysis attributes part of the original distinction to anecdotal observation, university competition and Kraepelin's authority; larger clinicopathological series later failed to demonstrate qualitative pathological separation.

Traditional schizophrenia subtypes similarly persisted in major diagnostic systems despite limited stability, reliability, validity, treatment specificity and longitudinal distinction.

Historical persistence and expert authority are therefore `HISTORICAL_OBSERVATION_ONLY`, not disease-division criteria.

### 6. Treatment response is highly informative but ontologically ambiguous

Target-specific responses strengthened APL, HER2-positive breast cancer and GIST because treatment effects aligned with reproducible underlying biology.

But treatment response can also define a clinically useful state rather than a different disease:

- drug-resistant epilepsy;
- MDR/RR tuberculosis;
- castration-resistant prostate cancer.

The framework therefore does not allow differential treatment response alone to establish a distinct disease. Its interpretation depends on temporality, treatment exposure and biological coherence.

### 7. Longitudinal instability has different meanings by classification type

Instability undermines a proposed stable disease subtype when membership changes unpredictably with symptom dominance or measurement, as in traditional schizophrenia subtypes.

Instability is expected for a genuine stage: a patient should be able to transition from one stage to another. CRPC is explicitly a treatment-emergent state, and MS phenotypes describe time-dependent course.

Therefore `stability` cannot be a universal yes/no criterion. The correct requirement is **temporal coherence appropriate to the proposed ontological class**.

### 8. Failed divisions repeatedly show three warning patterns

Across presenile/senile dementia, schizophrenia subtypes, old autism/PDD categorical partitions, low-renin hypertension as a single distinct entity, and SCLC over-subtyping, recurrent problems were:

1. weak or context-dependent boundaries;
2. low longitudinal/reclassification stability or reproducibility;
3. absence of distinctive prognosis, mechanism or treatment utility sufficient for the claimed ontology.

These negative controls materially shaped criteria U01, U03, U04, U05 and U06.

## Promoted criteria

The historical run promoted seven general requirements:

- U01 operationalizable/reproducible discriminator;
- U02 independent replication/transportability;
- U03 boundary robustness;
- U04 temporal coherence appropriate to classification type;
- U05 specificity beyond alternative explanations;
- U06 longitudinal/natural-history coherence appropriate to class;
- U07 clinical decision utility, explicitly supportive rather than sufficient for biological ontology.

It then generated separate gates for:

- DISTINCT_DISEASE;
- BIOLOGICAL_SUBTYPE_OR_ENDOTYPE;
- DISEASE_STAGE;
- TREATMENT_RESPONSE_STATE;
- OPERATIONAL_CLINICAL_CATEGORY.

See the frozen JSON for exact requirements.

## Historical observations deliberately NOT promoted into scientific criteria

The following remain controls or bias flags:

- expert consensus;
- regulatory recognition;
- duration of historical classification;
- war or political stability;
- national/global economic conditions;
- research funding;
- institutional capacity;
- technology availability;
- pharmaceutical/commercial incentives;
- reimbursement;
- advocacy;
- prestige/authority and institutional competition.

These variables can explain why a classification appeared, disappeared, spread or was delayed. They cannot by themselves show that the underlying entities are biologically distinct.

## Context-adjustment rule

For each historical case, two questions must remain separate:

1. Why was this division discovered or adopted at this historical moment?
2. Was the resulting division scientifically valid?

A context-dominant discovery history can still yield a scientifically valid split. Conversely, a science-intensive or prestigious historical classification can fail later validation.

No numeric percentage of `science versus context` is assigned unless the historical evidence supports such quantification. Current labels are qualitative and explicitly evidence-dependent.

## Face-validity rule

A recurrent historical feature is promoted only if it:

- has a coherent relation to disease ontology, course, mechanism, prognosis or treatment;
- can be operationalized across disorders;
- helps distinguish successful from failed classifications;
- is not merely an artefact of historical adoption or institutional authority;
- would produce an interpretable result if applied prospectively to a new target disorder.

Otherwise it remains `HISTORICAL_OBSERVATION_ONLY` or `CONTEXT_CONTROL`.

## Why v0.1 is frozen now

The current sample is sufficiently diverse to produce a testable framework, but not sufficiently exhaustive to claim a final universal theory of disease classification. Freezing v0.1 prevents downstream disease-specific reviews from adapting criteria to obtain a preferred result.

Future historical cases can generate v0.2, v0.3, etc. If an amendment changes a central criterion, any disease-specific conclusion affected by that criterion must be rerun under both the earlier and amended versions.

## Important limitations

- purposive rather than exhaustive historical sample;
- web-accessible and predominantly English-language evidence;
- uneven depth of historical scholarship between diseases;
- residual Western/wealthy-country bias despite inclusion of China and West Africa;
- economic context was not converted into historical GDP or expenditure covariates in this first run;
- contextual causal attribution is qualitative and is marked as uncertain when direct historical evidence is absent;
- some accepted categories remain scientifically evolving, particularly mechanistic endotypes and clinical-stage taxonomies;
- no attempt was made to calculate a single numerical disease-splitting score because the historical evidence argues against a class-agnostic score.

## Output for the disease-specific module

The disease-specific module should consume only the versioned frozen framework, not this narrative synthesis. It must report evidence criterion-by-criterion and choose the appropriate classification class before applying class-specific gates.

If a target disorder suggests a genuinely missing criterion, the target module may create an amendment candidate but cannot modify the historical framework itself.
