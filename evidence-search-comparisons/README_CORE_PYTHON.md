# Reusable Python Core

`institute_search` is the reusable engine for the Institute evidence-search methodology.

## Design rule

The Python package must remain domain-agnostic. Do not hard-code Alzheimer disease, dementia, BPSD, insulin signaling, depression, schizophrenia, or any future scientific topic into the core.

Domain knowledge belongs in:

1. base methodology JSON;
2. run-specific JSON/YAML overlays;
3. optional Python hooks implementing a documented protocol interface.

The first production use case is the brain-insulin-across-dementias project, but the same engine must be able to run a future oncology, psychiatry, neurology, or other evidence question without changing the orchestration kernel.

## What the core owns

- run state and resumable generation tracking;
- provenance-preserving directed evidence graph;
- publication versus study-family identity hooks;
- pruning state without deletion;
- novelty normalization;
- three-consecutive-zero-novel-insight saturation logic;
- resource-limited versus scientifically saturated distinction;
- process telemetry interfaces;
- deterministic dendrogram-like projection of the directed graph;
- config composition and validation;
- provider/search/model adapter interfaces as later modules.

## What domain configs own

- scientific question;
- competing models;
- evidence classes and directness hierarchy;
- disease/population strata;
- temporal ontology and pathology anchors;
- genetics and preclinical constructs;
- BPSD or other clinical phenotype layers;
- adaptive/pathological aging hypotheses;
- domain-specific novelty categories;
- domain-specific claim-block rules;
- required synthesis tables.

## Configuration composition

Use one reusable base configuration and one or more overlays:

```bash
institute-search validate \
  --config config/domain_agnostic_multiagent_search.json \
  --overlay config/dementia_brain_insulin_temporal_run.json \
  --overlay config/recursive_saturation_3_no_new_insight.json
```

Additional genetics, BPSD, evolutionary-aging, and visualization addenda can be overlaid without changing Python source.

## Core saturation invariant

Scientific saturation is not allowed before at least three consecutive completed cycles with zero qualifying new insight.

Any material, verified insight resets the streak to zero. Bibliographic novelty, duplicate publications, paraphrases, and LLM agreement alone do not reset it.

A resource stop is always `RESOURCE_LIMITED_NOT_SATURATED` unless the scientific stopping rule had already been met and separately audited.

## Graph and dendrogram

The source of truth is a directed graph. A reference may have multiple parents.

The dendrogram-like growth-and-pruning figure is a deterministic left-to-right projection for human review. Pruned nodes remain represented with pruning reasons and are never silently deleted.

## Development sequence

1. establish and test the reusable kernel;
2. add search-provider adapters;
3. add LLM/provider adapters;
4. add study-family resolution;
5. add extraction/appraisal hook registry;
6. add CSV/JSONL ledgers and resumability;
7. add Graphviz/SVG and interactive rendering;
8. run dementia project as the first end-to-end validation;
9. prove reusability by running a second unrelated scientific question with no core-code changes.

## Reusability acceptance criterion

The architecture is considered genuinely reusable only when a second domain can be executed by supplying configuration and hooks without modifying `engine.py`, `state.py`, `novelty.py`, or `graph.py`.
