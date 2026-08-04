# Historical Disease-Splitting Module — v0.2 Report

Run date: 2026-08-04
Framework output: `frozen_disease_splitting_framework_v0.2.json`

## Question

Across the history of medicine, what kinds and combinations of evidence support dividing an apparently unitary illness into distinct diseases, biological subtypes/endotypes, dimensions/spectra, longitudinal stages, treatment-response states or operational categories? Which proposed divisions fail, merge or require revision? How should socioeconomic, political, military, technological, institutional, commercial, regulatory and geographic context modify historical inference without being mistaken for biological evidence?

## Design

v0.2 prospectively stress-tested the frozen v0.1 framework with 19 additional classification events selected to challenge rather than confirm it. Together with the 21 v0.1 cases, the evidence map contains 40 historical comparators across endocrinology, infectious disease, oncology/hematology, neurology, rheumatology, respiratory medicine, gastroenterology, sleep medicine, psychiatry, critical care and cardiovascular medicine.

The sample remains purposive and systematic-style rather than exhaustive.

## Main result

The core v0.1 architecture survived: there is no historically coherent single score that should decide all forms of medical subdivision. The history continues to support universal validity requirements combined with class-specific gates.

v0.2 adds two scientific safeguards, one new positive classification class and several structural/contextual controls.

## 1. Continuous biology must have a positive destination

The Ridley-Jopling leprosy classification is the clearest historical demonstration. Clinical and pathological manifestations correlate with host immune response along a tuberculoid-to-lepromatous spectrum. The scientific success is the ordered continuum, not an assertion that each point on the continuum is a separate disease.

Axial spondyloarthritis and heart-failure EF categories reinforce the same problem: clinically useful cut-points can lie on continuous biology or physiology.

v0.1 warned that arbitrary thresholds weaken a disease split but did not specify what to conclude when the continuum itself is reproducible. v0.2 therefore adds `DIMENSION_OR_SPECTRUM`.

## 2. Strong biological ontology usually requires convergence

The strongest historical separations repeatedly show convergence across independent domains.

Examples include:

- CML: cytogenetics, BCR::ABL1 mechanism and target-specific therapy;
- APL: morphology/coagulopathy, t(15;17), PML::RARA and differentiation therapy;
- GIST: pathology/cell lineage, KIT/PDGFRA biology and imatinib sensitivity;
- NMOSD: AQP4-IgG, immunopathogenesis, phenotype, course and treatment implications;
- MODY: single-gene etiology, family pattern, beta-cell physiology and gene-specific treatment consequences;
- low-grade versus high-grade serous ovarian carcinoma: morphology, precursor pathways, molecular profiles, course and chemotherapy response.

By contrast, several failed or revised categories had one attractive discriminator but weak cross-domain coherence.

v0.2 therefore adds U08 `Convergent multi-domain coherence` for claims of distinct biological disease or mechanistic endotype. It is not a mechanical requirement to count a fixed number of domains; an exceptionally causal and specific discriminator can carry high weight if independently validated.

## 3. The residual-category problem is recurrent

A validated positive subgroup does not prove that its complement is one coherent entity.

Examples:

- narcolepsy type 1 has strong hypocretin/orexin biology, whereas type 2 lacks an equivalent positive marker and is less stable on repeated testing;
- seropositive RA shows stronger biological coherence than the heterogeneous seronegative remainder;
- T2-high asthma is biologically better characterized than the residual T2-low umbrella;
- papillary RCC type 2 proved heterogeneous enough that WHO 2022 removed the old type 1/type 2 binary scheme.

v0.2 therefore adds U09 `Positive-definition and residual-category caution`.

Terms such as marker-negative, non-A, NOS or unclassified may be clinically useful, but they remain provisional unless positive reproducible coherence emerges.

## 4. One disorder can legitimately have several simultaneous classifications

Historical classification is frequently multi-axial.

A malignancy can be a molecularly defined disease, possess an anatomical or biological stage, and later acquire a treatment-resistance state. CML is a clear example. Leprosy can be described along an immunological spectrum while acute reaction states are superimposed.

The final disease-specific module should therefore not force one winner when different axes answer different questions.

v0.2 adds `COMPOSITE_MULTIAXIAL`.

## 5. Historical context modifies negative inference

v0.1 established that war, economics, funding, technology, commercial incentives and institutional authority can alter discovery/adoption timing without proving biological validity.

v0.2 adds a further asymmetry: absence of evidence is less informative when the relevant population had little opportunity to generate evidence.

Type 5/malnutrition-related diabetes is an informative case. A lean, undernourished diabetes phenotype was described in tropical/low-resource populations for decades, received WHO classification in 1985, was removed in 1999 amid uncertainty regarding causation, and was re-recognized in 2025 as new metabolic investigations suggested physiology not typical of autoimmune type 1 or insulin-resistant type 2 diabetes. The modern entity remains scientifically contested.

This history does not prove that type 5 diabetes is a distinct disease. It does demonstrate that sparse evidence from neglected populations cannot be interpreted the same way as repeated negative investigations in well-resourced populations.

v0.2 therefore adds H07 `Research-opportunity asymmetry`.

## 6. Geography can be an observation before it becomes a misleading taxonomy

Burkitt lymphoma illustrates both successful discovery and later correction. Geographic patterns in equatorial Africa helped identify the disease and its environmental/viral associations. Yet later molecular classifications indicate that EBV-positive versus EBV-negative biology may cut across the traditional endemic/sporadic/immunodeficiency-associated categories.

Geography can generate a scientifically productive hypothesis without being the final biological boundary.

The disease-specific module must therefore distinguish environmental/geographic causal evidence from geography used merely as a proxy.

## 7. Re-merging is evidence too

The historical module must learn from simplification as well as subdivision.

v0.2 added several examples:

- papillary RCC type 1/2 was abandoned as a binary molecularly coherent scheme;
- Sepsis-3 removed the redundant `severe sepsis` category and changed the conceptual basis of sepsis definitions;
- historical Burkitt epidemiologic subtypes are being superseded by more biologically aligned classifications;
- older autism and SCLC subtype histories in v0.1 already demonstrated merger/simplification after poor reproducibility.

A methodology that only searches for successful splits is structurally biased toward subdivision.

## 8. Treatment response remains powerful but ontologically conditional

The expanded cases reinforce the v0.1 rule.

Mechanism-aligned response in driver-defined NSCLC, GIST, HER2-positive breast cancer or APL strongly supports a biological subtype because the treatment interaction converges with independent biology.

In contrast, treatment-resistance states such as drug-resistant epilepsy remain valid clinical states without becoming separate pretreatment diseases.

Treatment response is therefore interpreted through temporality and mechanism rather than used as a standalone disease criterion.

## 9. Jurisdiction-specific adoption is a separate variable

WHO, professional societies, national regulators and health systems can adopt or abandon categories at different times. Decisions may reflect available diagnostic technology, service structure, reimbursement, local epidemiology or evidence standards.

v0.2 adds H08 `Jurisdictional adoption divergence`. A classification decision by one authority is recorded as an adoption event, not automatically as evidence of universal biological ontology.

## 10. Target-family holdout prevents subtle circularity

Because some historical comparators may be close to a future target, v0.2 requires sensitivity analysis excluding the target's own disease family from criterion derivation/interpretation.

For example, a future schizophrenia review should not be able to satisfy or fail the framework simply because traditional schizophrenia subtypes and the Kraepelinian psychosis boundary were themselves historical comparators. The review should report conclusions both with and without those close comparators.

## v0.2 scientific criteria

v0.2 retains U01-U07 and adds:

- U08 convergent multi-domain coherence for strong biological-ontology claims;
- U09 positive-definition/residual-category caution.

It adds class-specific logic for:

- `DIMENSION_OR_SPECTRUM`;
- `COMPOSITE_MULTIAXIAL` outputs.

See the frozen JSON for exact operational wording.

## Historical/context variables not promoted to intrinsic disease criteria

The following remain context controls or adoption markers:

- national or global economic conditions;
- war and political instability;
- research funding;
- institutional prestige and authority;
- technology availability;
- commercial incentives;
- regulatory recognition;
- reimbursement;
- advocacy;
- duration of historical classification;
- geographic concentration by itself;
- absence of research in a neglected population.

These can explain evidence production and adoption. They cannot by themselves establish a disease split.

## Face-validity rule retained

A historical feature is promoted only when it has coherent scientific relevance, can be operationalized across disorders, helps discriminate successful from failed/revised classifications, and would yield an interpretable prospective result.

Otherwise it is retained as `HISTORICAL_OBSERVATION_ONLY` or `CONTEXT_CONTROL`.

## Freeze decision

v0.2 is frozen for downstream testing. The framework has changed enough to justify a new version but not enough to invalidate the basic v0.1 architecture.

Future historical expansion must create v0.3 or later. Disease-specific modules may submit amendment candidates but may not edit v0.2.

## Limitations

- purposive rather than exhaustive historical sampling;
- predominantly English-language and web-accessible evidence;
- uneven quality of historical scholarship across cases;
- no formal quantitative causal model for war, GDP, research spending or institutional capacity;
- no attempt to estimate a percentage of a classification decision attributable to science versus context;
- contemporary/evolving entities such as MOGAD, ANCA-based vasculitis reclassification and type 5 diabetes remain moving targets;
- classification events are units of historical comparison, not independent epidemiologic effect estimates;
- search and synthesis were performed by one model using sequential roles rather than genuinely independent agents;
- token and monetary-cost telemetry are unavailable from the present environment and are therefore not estimated.

## Output rule

The disease-specific module should consume `frozen_disease_splitting_framework_v0.2.json` as the immutable judging framework. Narrative historical reports provide provenance but must not be allowed to change the downstream criteria silently.