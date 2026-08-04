# Report 3: Process Metrics and Cost Scenarios

Comparison of the two simulated research pipelines
Rapid evidence synthesis and methodological simulation | Search date: July 31, 2026

## What was measured versus estimated

Measured in this run: four initial topic-search blocks, two targeted follow-up blocks, one Co-Scientist architecture search block, one pricing block, six candidate explanatory models, six critique reports and two final synthesis pipelines. Search-result counts are not database yield counts because web search does not expose a reproducible PubMed-style total for every query.

Estimated: model tokens, runtime and API cost. The ChatGPT environment does not expose exact per-turn token accounting, and Google does not publish the token consumption or price of the proprietary Hypothesis Generation experiment. Estimates below are implementation scenarios, not invoices.

## Process comparison

| Metric | Simulated Co-Scientist | Clinical model pipeline |
|---|---|---|
| Primary optimization target | Novelty, plausibility, testability and proposal quality | Diagnostic discrimination, evidentiary traceability and clinical applicability |
| Initial models | 6 | 5 retained clinical alternatives |
| Formal critique units | 6 hypothesis-specific reviews | Claim-by-claim evidentiary audit |
| Ranking | Tournament rank 1-6 | No forced rank until patient data are available |
| Evolution | Top model refined into 4 stages | Models preserved; assessment determines updating |
| Null/artefact protection | Included as H6 | Mandatory and operationalized |
| Main output | Novel mixed hypothesis plus study protocol | Differential formulation plus testing sequence |
| Primary failure risk | Interesting hypothesis mistaken for likely diagnosis | Conservative output that generates less novelty |

## Token-budget scenarios

| Stage | Lean run | Standard run | Extended run |
|---|---|---|---|
| Evidence retrieval and extraction | 60k input / 12k output | 180k / 35k | 600k / 100k |
| Hypothesis generation | 20k / 12k | 70k / 35k | 220k / 100k |
| Critique and tournament | 35k / 18k | 150k / 70k | 600k / 250k |
| Evolution and meta-review | 20k / 10k | 80k / 30k | 280k / 100k |
| Audit and final reports | 25k / 12k | 90k / 35k | 300k / 100k |
| Total | 160k input / 64k output | 570k / 205k | 2.00M / 650k |

## Illustrative API cost

Cost formula: input tokens / 1,000,000 x input rate + output tokens / 1,000,000 x output rate. Web retrieval, embeddings, storage and orchestration are additional.

Illustration used Google Cloud list prices retrieved July 31, 2026 for Gemini 3.1 Pro Preview at USD 2 per million input tokens and USD 12 per million output tokens for contexts at or below 200,000 tokens per request. Actual Co-Scientist access, enterprise pricing, caching, long-context tiers and future prices may differ.

| Scenario | Input cost | Output cost | Illustrative model total |
|---|---:|---:|---:|
| Lean: 160k in / 64k out | $0.32 | $0.77 | $1.09 |
| Standard: 570k in / 205k out | $1.14 | $2.46 | $3.60 |
| Extended: 2.00M in / 650k out | $4.00 | $7.80 | $11.80 |

## Likely relative resource use

| Pipeline | Estimated token multiplier | Reason |
|---|---:|---|
| Clinical model only | 1.0x baseline | Fewer generative branches; more structured extraction and audit. |
| Co-Scientist-style simulation | 1.5-3.0x | Pairwise comparisons, repeated critiques and evolutionary rounds. |
| Combined recommended system | 1.8-3.5x | Shared evidence map reduces duplication, but both novelty tournament and clinical audit remain. |

## Quality and efficiency metrics for future runs

- Citation validity: percentage of sampled claims actually supported by the cited source.
- Relationship support: percentage of causal edges directly demonstrated versus inferred.
- Hypothesis diversity: proportion of models that make genuinely different predictions.
- Discriminability: number of tests for which leading models predict different outcomes.
- Counterevidence coverage: contradictory or null study families divided by all included study families.
- Model survival: generated, merged, rejected and retained hypotheses by cycle.
- Human correction burden: substantive corrections per 1,000 final words.
- Cost per retained discriminating hypothesis and cost per verified claim.
- Time to evidence saturation and duplicate yield in the last two cycles.
- Clinical actionability: whether the distinction would change investigation, management or treatment.

## Recommended default configuration

Use one shared evidence map, generate six models, cluster near-duplicates, run one critique per model, use a limited pairwise tournament only for the top four, and then apply the full clinical evidence audit to the top models plus the null/artefact model. This preserves most of the benefit while controlling token growth. Escalate to an extended run only if a new experiment, grant or publication-level hypothesis is the objective.

## Pricing reference

Google Cloud generative AI pricing, accessed July 31, 2026. Google Gemini Developer API pricing.
