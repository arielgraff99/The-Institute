# Codex Addendum: Three Consecutive Zero-New-Insight Cycles

## Authority

This addendum overrides any earlier stopping language that permits scientific saturation after two low-yield cycles or after a fixed maximum number of generations.

Load:

`evidence-search-comparisons/config/recursive_saturation_3_no_new_insight.json`

as an authoritative stopping-rule override for the brain-insulin-across-dementias project and its genetics, evolutionary/adaptive-aging, temporal, preclinical, and BPSD layers.

## Core rule

Recursive generation must continue until **at least three consecutive completed and audited cycles produce zero qualifying novel insight**.

A fixed generation count may be used only as a resource review point. It may not be used to declare scientific saturation.

If execution terminates before the three-cycle criterion because of cost, access, API, computational, time, or other resource limits, emit:

`RESOURCE_LIMITED_NOT_SATURATED`

and report the current zero-insight streak.

## Cycle semantics

Cycle 0 is protocol/reconnaissance and does not count toward the zero-insight saturation streak.

For Cycle 1 onward:

1. execute planned search and recursive citation expansion;
2. deduplicate publications and link study families;
3. extract scientific results;
4. perform risk-of-bias and measurement-validity audit;
5. perform contradiction/null/replication audit;
6. perform temporal/onset audit;
7. perform genetics and variant-to-function preclinical audit;
8. perform adaptive-versus-pathological aging audit;
9. perform BPSD phenotype/trajectory audit;
10. update model comparison;
11. only then adjudicate whether the cycle contains a novel insight.

A partial, failed, or unaudited cycle can never increment the saturation streak.

## Novel insight

A new paper is not automatically a new insight.

A qualifying insight is verified information that changes, extends, challenges, localizes, temporally reorders, validates, invalidates, or materially changes confidence in the evidence map or competing models.

Qualifying categories include:

- new independent eligible study-family evidence;
- independent replication that changes confidence;
- material contradiction or null result;
- new molecular mechanism, pathway node, direction, cellular compartment, or brain region;
- new dementia pathology or subtype distinction;
- common polymorphism, rare/pathogenic variant, polygenic signal, colocalization, genetic correlation, MR result, or other genetic evidence changing interpretation;
- genotype-defined or genetically induced preclinical variant-to-function evidence;
- evidence separating genetic susceptibility from functional expression;
- earlier or differently ordered temporal evidence;
- evidence changing whether an insulin-signaling phenotype precedes or follows proteinopathy, vascular pathology, synaptic dysfunction, energetic failure, or neuronal loss;
- evidence that an insulin-signaling change is adaptive, neutral, maladaptive, compensatory, or pathological rather than simply abnormal;
- BPSD symptom, cluster, subtype, trajectory, or behavioral phenotype that changes cross-dementia interpretation;
- clinically meaningful genotype x pathology x insulin x BPSD interaction;
- treatment interaction discriminating models;
- new confounder, mediator, effect modifier, or collider materially altering inference;
- assay-validation/invalidation, correction, retraction, registry discrepancy, or missing-evidence result changing confidence;
- a newly discovered terminology/construct only if it opens a genuinely new evidence branch;
- a new high-information discriminator or testable prediction;
- any material change in model viability or final adjudication.

The following do not reset the counter by themselves:

- duplicate publications;
- review articles restating the same underlying evidence;
- additional citations with no new result;
- wording changes or relabeling;
- LLM agreement;
- minor bibliographic corrections without inferential impact;
- repeated evidence from the same study family without a distinct new result.

## State-machine requirement

Implement persistent saturation state, for example:

```python
@dataclass
class SaturationState:
    consecutive_zero_insight_cycles: int = 0
    saturated: bool = False
    stop_reason: str | None = None


def update_saturation(state: SaturationState, audit: CycleNoveltyAudit) -> SaturationState:
    if not audit.completed or not audit.fully_audited:
        return state

    if audit.novel_insight_count > 0:
        state.consecutive_zero_insight_cycles = 0
    else:
        state.consecutive_zero_insight_cycles += 1

    if (
        state.consecutive_zero_insight_cycles >= 3
        and audit.all_additional_stop_conditions_met
    ):
        state.saturated = True
        state.stop_reason = "THREE_CONSECUTIVE_ZERO_NOVEL_INSIGHT_CYCLES"

    return state
```

Persist this state after every durable cycle so resume operations do not lose or falsely restart the saturation streak.

## Required novelty audit

Create one row per cycle in:

`cycle_novelty_audit.csv`

At minimum include:

- cycle ID and generation number;
- new records;
- new eligible independent study families;
- new independent replications;
- material contradictions/null findings;
- molecular/mechanistic insights;
- genetic insights;
- preclinical variant-to-function insights;
- temporal insights;
- adaptive-versus-pathological insights;
- BPSD insights;
- measurement-validity insights;
- missing-evidence insights;
- new discriminators;
- model-confidence changes;
- adjudication changes;
- total qualifying novel insights;
- zero-insight boolean;
- consecutive zero-insight streak;
- reset reason;
- unresolved high-priority branches;
- blocked claims still requiring search;
- audit completion status and timestamp.

Also generate:

- `saturation_trace.json`
- `stopping_decision.md`

## Tests

Add tests proving:

1. two consecutive zero-insight cycles cannot stop the run;
2. three consecutive fully audited zero-insight cycles can stop only when additional stop conditions are met;
3. any qualifying insight resets the counter to zero;
4. duplicate papers do not reset the counter;
5. independent replication that changes confidence does reset the counter;
6. new earlier temporal evidence resets the counter;
7. new genetic or variant-to-function evidence resets the counter;
8. new BPSD phenotype/trajectory evidence resets the counter;
9. assay invalidation affecting a central claim resets the counter;
10. partial or failed cycles do not increment the counter;
11. resume preserves the previous saturation streak;
12. reaching a resource review point before saturation yields `RESOURCE_LIMITED_NOT_SATURATED`, never `SATURATED`.

## Acceptance criterion

No final report may state that the literature search reached saturation unless the provenance log demonstrates three consecutive completed, fully audited cycles with zero qualifying novel insight and all additional stopping conditions were met.
