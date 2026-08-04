# Depression Disease-Specific Review Module v1.0 — First Executable Run

Run date: 2026-08-04  
Historical ruler: frozen Historical Disease-Splitting Framework v0.2  
Scope: sentinel implementation run; not an exhaustive systematic review.

## Primary result

The run does **not** support treatment-resistant depression (TRD) as one distinct disease biologically separate from other major depressive disorder (MDD). It also does **not** support the entire TRD category as one coherent biological endotype.

The best-fitting representation is **COMPOSITE_MULTIAXIAL**:

1. **OPERATIONAL_CLINICAL_CATEGORY — SUPPORTED.** TRD has reproducible operational definitions, major burden, and a distinct later-line care pathway.
2. **TREATMENT_RESPONSE_STATE — PARTIALLY SUPPORTED / STRONGLY FAVORED CONCEPTUALLY.** The state follows treatment exposure and is meaningful when adequacy and pseudoresistance are assessed; however, pseudoresistance is not consistently excluded in the literature.
3. **DIMENSION_OR_SPECTRUM — PARTIALLY SUPPORTED.** Resistance probability and prognosis vary with accumulated failures, chronicity, severity, recurrence and function, while the common two-failure threshold behaves as an operational cut-point rather than a demonstrated biological discontinuity.
4. **DISEASE_STAGE — PARTIALLY SUPPORTED.** Successive failure and poorer longitudinal outcome create a stage-like component, but this cannot explain all cases because baseline endotypes, diagnostic heterogeneity, access and treatment-exposure factors also contribute.
5. **BIOLOGICAL_SUBTYPE_OR_ENDOTYPE — NOT SUPPORTED AS THE GLOBAL TRD CLASS.** Candidate inflammatory, genetic, imaging and molecular subgroups exist, but none maps reproducibly onto all TRD; some may cut across TRD and non-TRD MDD.
6. **DISTINCT_DISEASE — NOT SUPPORTED.** Boundary robustness and a stable intrinsic etiologic/pathological/mechanistic discriminator are not met.

## Why the distinct-disease gate failed

- Different TRD definitions identify materially different populations.
- Most biomarker studies measure patients after substantial illness and treatment exposure.
- Genetics shows inherited enrichment but substantial overlap with MDD and other psychiatric liability rather than a clean discontinuity.
- Imaging findings are heterogeneous and not externally validated as a clinical classifier.
- Inflammation has treatment-moderating and subgroup signals, but no validated universal pretreatment TRD biomarker.
- Transcriptomic findings are promising discovery evidence but remain treatment-exposed and require independent prospective replication.

## Why a treatment-state / dimension / stage mixture survived

Sequential-treatment data show declining remission and increasing relapse with additional treatment steps. Across clinical cohorts, chronicity, severity, recurrence, hospitalization and functional impairment repeatedly predict resistance. Operational definitions and expert consensus also explicitly use treatment exposure to assign TRD. At the same time, health-system variables, adherence, treatment adequacy and access can influence who reaches the label.

## Context-adjusted interpretation

TRD is scientifically real as an observed treatment-course problem, but the probability of receiving the label is partly shaped by the healthcare environment. Treatment availability, adequacy, adherence assessment, specialist access, socioeconomic disadvantage, provider behavior and delay to effective care can all change observed resistance. These contextual factors weaken inference that treatment failure automatically identifies a new biological disease. They do not make the clinical state unreal.

## Restriction sensitivity

The unrestricted and higher-confidence tracks produced the same class-level ordering. Removing discovery-stage/cross-sectional evidence weakened confidence in biological-endotype claims but did not convert TRD into a distinct disease or erase its operational/treatment-state character.

## Decisive missing evidence

The most informative future design remains a treatment-naive, first-episode MDD cohort with repeated multi-omic, immune, metabolic, imaging, physiological, cognitive, sleep, pharmacokinetic, adherence and socioeconomic measurement; standardized adequate sequential treatments; externally validated baseline subgroup discovery; and randomized biomarker-by-treatment interaction testing.

## Current classification

**Preferred:** COMPOSITE_MULTIAXIAL  
**Strongest axis:** OPERATIONAL_CLINICAL_CATEGORY  
**Next strongest:** TREATMENT_RESPONSE_STATE + DIMENSION_OR_SPECTRUM  
**Contributing in a subset:** DISEASE_STAGE + MULTIPLE BIOLOGICAL ENDOTYPES  
**Not established:** ONE DISTINCT TRD DISEASE

## Integrity limitation

This is the first executable implementation, using 30 purposively selected sentinel records from 28 study families plus prior Institute evidence maps. It validates the software/data contract and produces a scientifically interpretable result, but it is not yet the full recursive, registry-complete, database-systematic depression run.
