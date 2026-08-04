# Depression Module v1.0 to v2.0 Delta

## Scientific purpose

v2.0 changes the unit of reasoning from a mostly binary TRD-versus-non-TRD comparison to a causal treatment-course representation. The frozen historical v0.2 ruler remains unchanged.

## Five implemented upgrades

1. **Treatment trajectory representation** — each evidence record is located on the treatment course (pre-treatment, first-line, multiple failures, advanced intervention, mixed/unknown). This prevents a post-ECT TRD biomarker from being treated as equivalent to a first-episode pretreatment predictor.
2. **Temporality engine** — biological findings are classified as baseline/predisposing, pre-resistance predictors, emerging-resistance findings, established-TRD correlates, or post-treatment/consequence-uncertain findings.
3. **Pseudoresistance and alternative-cause engine** — treatment adequacy, adherence and major alternative explanations are represented explicitly; R02 is recomputed conservatively from the evidence ledger.
4. **Endotypes independent of TRD** — the system searches for MDD-wide or cross-cutting biological subtypes first, then asks whether any map onto resistance. Five recent sentinel records were added specifically for this test.
5. **Non-psychiatric historical holdout** — HIST008 (schizophrenia subtypes), HIST019 (PDD/autism merger) and HIST035 (Kraepelinian psychosis boundary) are removed from criterion support. Every promoted scientific criterion retained explicit non-psychiatric historical support, producing sensitivity ruler v0.2-H1.

## Gate hardening

v2.0 generalizes the adjudicator to enforce `required + any explicit CORE criteria` so it remains correct when consuming either a compact interface snapshot or the full historical framework. The v1.0 compact interface had already promoted D01, E01, Q01/Q02, S01, R01/R02 and O01 into its `required` lists, so this hardening does **not** reveal a missed v1.0 gate and does not change the v1.0 conclusion.

## Evidence-set change

- v1.0: 30 records / 28 study families.
- v2.0: 35 records / 33 study families.
- Five additions were targeted to the new architecture rather than to maximize agreement with the prior conclusion: episode-wide Maudsley staging; MDD neuroimaging/multi-omics subtypes; independently validated metabolomic subtypes; immune/metabolic multi-omics subtypes associated with antidepressant response; and a systemic type-2 immune signal in MDD.

## Result change

The overall TRD classification remains COMPOSITE_MULTIAXIAL. The important change is conceptual: E01 is now met for the proposition that **biological endotypes exist within MDD**, while U03 remains not met for the proposition that **TRD itself is one biological endotype**. Thus biological heterogeneity is promoted without converting the residual treatment-response label into a biological disease.
