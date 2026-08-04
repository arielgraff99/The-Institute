# Reusable Python Core Architecture

## Goal

Implement the evidence-search system as an installable, reusable Python package. The dementia and brain-insulin project is the first profile, not the core itself.

## Strict separation

Reusable logic belongs under `src/institute_search/`. Project-specific terminology, models, stages, pathology anchors, genetics, BPSD definitions, novelty rules and outputs belong under `profiles/<profile_name>/`.

The reusable core must not hard-code Alzheimer disease, dementia, insulin resistance, BPSD, APOE or any other project-specific concept.

## Target structure

```text
evidence-search-comparisons/
  pyproject.toml
  src/institute_search/
    __init__.py
    cli.py
    config.py
    schemas.py
    orchestrator.py
    state.py
    provenance.py
    search/
    llm/
    extraction/
    appraisal/
    graph/
    metrics/
    synthesis/
    plugins/
  profiles/
    dementia_brain_insulin/
      profile.json
      model0_genetics.json
      adaptive_aging.json
      bpsd.json
      saturation.json
      visualization.json
      prompts/
  tests/
```

## Core subsystems

### Configuration engine

- Load core defaults, domain-agnostic methodology, project profile, addenda and command-line overrides.
- Deep-merge with explicit precedence and conflict logging.
- Validate before external calls.
- Save the resolved configuration and hashes into every run.

### Search engine

- Provider-neutral search adapters.
- Exact query provenance.
- Backward and forward citation expansion.
- Author, terminology, registry, protocol, correction and retraction routes.
- Resumable pagination.

### LLM orchestration

- Provider-neutral model adapter interface.
- At least three model families when configured.
- Isolated role passes for discovery, extraction, appraisal, contradiction audit and synthesis.
- LLM agreement never counts as scientific replication.

### Evidence and study-family ledger

- Separate publication identity from study-family identity.
- Preserve included, excluded, duplicate, unresolved, inaccessible, blocked and unpublished records.
- Track claims supported and contradicted, risk of bias, missing evidence and token attribution.

### Plugin interface

Profiles may register domain-specific extractors and validators through a generic interface:

```python
class DomainPlugin(Protocol):
    name: str

    def validate_profile(self, config: dict) -> list[str]: ...
    def build_seed_queries(self, config: dict) -> list[QuerySpec]: ...
    def extract_domain_fields(self, record: SourceRecord) -> dict: ...
    def classify_novel_insight(self, previous: RunState, current: RunState) -> list[Insight]: ...
    def build_domain_outputs(self, run_dir: Path) -> None: ...
```

The dementia profile supplies plugins for insulin evidence directness, temporal ordering, genetics and preclinical models, adaptive versus pathological aging, and BPSD phenotypes.

### Generic temporal engine

The core supports arbitrary stage vocabularies and multiple clocks supplied by the profile. It distinguishes observed from inferred onset, longitudinal from cross-sectional evidence, and clinical from pathological timing.

The dementia profile configures clinical, pathology, genetic-susceptibility and BPSD-trajectory clocks.

### Novelty and stopping engine

- Compare each completed cycle with cumulative prior evidence.
- Distinguish bibliographic novelty from scientific novelty.
- Reset the streak whenever a verified qualifying insight appears.
- Require three consecutive completed zero-novel-insight cycles when configured.
- Label forced termination as `RESOURCE_LIMITED_NOT_SATURATED`.

### Graph and dendrogram renderer

The canonical representation is a directed graph. The renderer produces record-level and study-family-compressed graphs, left-to-right growth-and-pruning projections, branch-efficiency views, generation summaries, stopping panels and optional interactive HTML.

All colors, shapes, pruning codes and growth triggers are profile-configurable.

### Metrics and resumability

- Provider-reported token usage when available.
- Run-specific pricing snapshots.
- Per-call, per-cycle, per-role and per-branch cost.
- Malfunction manifest and retries.
- Durable checkpoints so failed calls do not restart completed work.

## Generic CLI

```bash
institute-search validate --profile profiles/dementia_brain_insulin
institute-search plan --profile profiles/dementia_brain_insulin --dry-run
institute-search run --profile profiles/dementia_brain_insulin --output runs/<run_id>
institute-search resume --run runs/<run_id>
institute-search render-graph --run runs/<run_id>
institute-search audit-saturation --run runs/<run_id>
institute-search summarize-cost --run runs/<run_id>
```

## Reuse rule

A new topic should require a new profile folder only, for example:

```text
profiles/depression_entities/
profiles/confabulation_vs_delusion/
profiles/amyloid_tdcs/
profiles/dementia_brain_insulin/
```

No core Python file should change unless the new project requires a genuinely reusable new capability.

## Packaging

Use Python 3.11 or later and `pyproject.toml`. Recommended dependencies are `pydantic`, `pandas`, `networkx`, `httpx`, `typer` or `argparse`, and `pytest`. Graphviz, pydot, pyvis and provider SDKs should be optional extras.

## Acceptance criteria

1. The dementia profile runs without domain-specific hard-coding in the core.
2. A second fixture profile runs using the same package.
3. Graph, metrics, saturation and provenance engines are shared across profiles.
4. Offline tests and dry-run require no paid API.
5. The package installs with `pip install -e .`.
6. The CLI validates, plans, runs, resumes, renders and audits a project.
7. Every run is reproducible from resolved config, hashes, logs, package version and Git commit SHA.
