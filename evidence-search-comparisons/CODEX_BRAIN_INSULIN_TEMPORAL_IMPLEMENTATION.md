# Codex Implementation Brief: Brain Insulin Resistance Across Dementias with Temporal Analysis

## Objective

Extend `evidence-search-comparisons/` into an executable, auditable, provider-neutral evidence-search engine for the project:

**Brain insulin resistance across dementias: shared mechanism, disease-specific phenotype, or downstream consequence?**

The implementation must answer two linked questions:

1. Is the phenomenon historically called "type 3 diabetes" biologically the same across dementias?
2. When does insulin-signaling dysfunction first become demonstrable in each dementia, relative to clinical stage and defining pathology?

Treat "type 3 diabetes" as a historical/conceptual label, not as an accepted diagnosis. The implementation must operationalize brain insulin resistance using directness of evidence and biological compartment rather than terminology alone.

## Existing repository sources of truth

Use, do not overwrite, the existing methodology:

- `evidence-search-comparisons/prompts/Deep_Search_with_Classification_Prompt.md`
- `evidence-search-comparisons/prompts/master_orchestration_prompt.md`
- `evidence-search-comparisons/config/institute_search_config.json`
- `evidence-search-comparisons/config/process_metrics_template.json`

Add and use:

- `evidence-search-comparisons/config/dementia_brain_insulin_temporal_run.json`

If `domain_agnostic_multiagent_search.json` becomes available in the repository, treat it as the reusable methodological base and the dementia file as the run-specific override. Do not silently rewrite the base protocol.

## Non-negotiable scientific constraints

1. Keep at least five competing scientific models viable at initialization. Do not optimize the search toward Alzheimer disease.
2. Maintain separate evidence units for publications and study families. Scientific replication is counted only across independent study families, cohorts/datasets, laboratories, or analytic pipelines.
3. At least three distinct LLM/model families must be usable when configured. Their agreement is quality control, not scientific replication.
4. Separate direct human-brain insulin evidence from peripheral insulin resistance, vascular/endothelial signaling, glial signaling, and neuronal signaling.
5. HOMA-IR, fasting insulin, HbA1c, TyG, diabetes diagnosis, or FDG-PET hypometabolism do not by themselves establish brain insulin resistance.
6. Search supporting, contradictory, null, replication, measurement-validity, retraction/correction, protocol/registry, and unpublished evidence streams.
7. Preserve all excluded, duplicate, inaccessible, blocked, corrected, retracted, and unpublished records with reasons.
8. Never infer temporal precedence from a cross-sectional severity association.
9. Never equate earliest observed abnormality with biological onset.
10. Claims about onset must be auditable back to study design, disease stage, pathology status, and measurement method.

## Proposed Python package

Create:

```text
evidence-search-comparisons/
  src/institute_search/
    __init__.py
    cli.py
    config.py
    schemas.py
    orchestrator.py
    search/
      __init__.py
      base.py
      pubmed.py
      crossref.py
      openalex.py
      semantic_scholar.py
    llm/
      __init__.py
      base.py
      openai_adapter.py
      anthropic_adapter.py
      google_adapter.py
    extraction/
      __init__.py
      normalize.py
      study_family.py
      insulin_evidence.py
      temporal.py
      measurement_validity.py
    appraisal/
      __init__.py
      routing.py
      claim_blocks.py
      missing_evidence.py
    graph/
      __init__.py
      citation_graph.py
      rendering.py
    metrics/
      __init__.py
      token_usage.py
      cost.py
      run_manifest.py
    synthesis/
      __init__.py
      model_comparison.py
      temporal_synthesis.py
      report.py
  tests/
    fixtures/
    test_config.py
    test_insulin_directness.py
    test_temporal_rules.py
    test_study_family.py
    test_replication.py
    test_saturation.py
    test_graph.py
    test_metrics.py
  pyproject.toml
```

Use standard-library functionality where practical. Reasonable dependencies include `pydantic`, `pandas`, `networkx`, `requests`/`httpx`, and `graphviz` or `pydot`. Keep optional visualization dependencies optional.

## Configuration model

Load the run-specific JSON and validate it before any external call.

Validation must fail if:

- fewer than three genuinely distinct scientific models exist;
- scientific models have no discriminating predictions;
- temporal analysis is enabled but temporal stages or claim classes are absent;
- model execution requires three LLM families but fewer than three configured adapters are available for a live multi-model run;
- percentage allocation does not sum to 100;
- required output names collide;
- a claim-block rule is malformed.

Support `--dry-run` to validate config, render planned queries, create empty ledgers, and estimate call topology without issuing paid/model/network requests.

## LLM/provider abstraction

Implement a common interface:

```python
class ModelAdapter(Protocol):
    provider: str
    model: str
    def generate(self, role: str, messages: list[dict], **kwargs) -> ModelResult: ...
```

`ModelResult` must include, when available:

- provider
- model
- model version/snapshot
- request/run identifier
- input tokens
- output tokens
- cached tokens
- latency
- status
- error
- retry count
- raw provider usage metadata

Do not fabricate unavailable usage fields. Use `null` plus a named estimation method if token estimation is explicitly enabled.

Do not hard-code current API prices into code. Load a run-specific `pricing_snapshot.json` or accept CLI pricing overrides so historical cost calculations remain reproducible.

## Search adapters

Implement search adapters independently from LLM adapters. A search source returns structured records and exact query provenance.

Minimum fields per search event:

- query_id
- exact query string
- source/database
- filters
- run timestamp
- result count only if the source returns it directly
- pagination information
- error/retry metadata

Do not claim database coverage that was not actually executed.

A useful initial implementation can support PubMed plus at least one citation/metadata source such as Crossref or OpenAlex. Keep additional sources pluggable.

## Study-family identity and deduplication

Represent publication identity separately from study-family identity.

Use deterministic matching clues:

- DOI/PMID/registry ID
- author overlap
- cohort name
- recruitment dates/sites
- sample size and group structure
- intervention/exposure
- dataset accession
- protocol linkage

Never merge solely because titles are similar. If uncertain, mark `study_family_status="unresolved"` and preserve both candidate records.

Multiple reports from one study family may strengthen extraction confidence but must not increment replication count.

## Brain-insulin evidence classification

Implement the evidence hierarchy from the run config.

At extraction, assign:

- biological compartment: systemic, vascular/endothelial, glial, neuronal
- evidence directness: A-F
- functional response demonstrated: yes/no/uncertain
- brain region/tissue
- cell type
- pathway nodes
- direction of abnormality
- systemic diabetes/metabolic status

Hard validation examples:

- HOMA-IR -> cannot classify above peripheral evidence unless an independent brain measure is also present.
- FDG-PET hypometabolism alone -> cannot be labelled functional brain insulin resistance.
- Static IRS1 abundance/phosphorylation -> molecular signaling evidence, but functional insulin resistance requires an insulin-response design or another justified functional assay.

## Temporal analysis: first-class subsystem

Create `extraction/temporal.py` and `synthesis/temporal_synthesis.py`. Temporal analysis is mandatory for this run.

### Canonical stages

Normalize study participants into the closest defensible stage:

1. cognitively normal, biomarker negative/unknown
2. preclinical biological disease
3. subjective cognitive decline
4. prodromal/MCI
5. established dementia
6. advanced disease

Preserve disease-specific labels in a separate field. Do not erase source terminology.

### Pathology anchors

Track temporal relation to:

- amyloid-beta
- tau
- alpha-synuclein
- TDP-43
- cerebrovascular injury
- neuroinflammation
- synaptic dysfunction
- mitochondrial/energetic dysfunction
- neuronal loss

### Temporal claim classes

Implement exactly:

- `T1_direct_precedence`: longitudinal evidence demonstrates insulin abnormality before a defined pathology, clinical transition, or neurodegenerative endpoint.
- `T2_anchored_early_presence`: direct observation in a preclinical/prodromal stage without demonstrated precedence over pathology.
- `T3_stage_association_only`: cross-sectional or stage-correlated evidence without onset inference.
- `T4_retrospective_or_proxy`: timing inferred from retrospective reports, peripheral proxies, unvalidated biomarkers, or indirect measures.
- `T5_onset_unresolved`: onset cannot be located defensibly.

### Temporal hard rules

Programmatically enforce:

1. Cross-sectional studies cannot generate `T1_direct_precedence`.
2. A biomarker observed in MCI does not prove it began in MCI.
3. An abnormality observed years before diagnosis can precede diagnosis while still occurring after molecular pathology; maintain both clocks separately.
4. If timing depends on an assay later shown to lack assumed biological specificity, downgrade temporal confidence and route to measurement-validity audit.
5. If only peripheral measures are available, do not create a brain-insulin onset claim.
6. Use `ONSET_UNRESOLVED` rather than interpolating a biological onset age.

### Temporal ledger schema

At minimum:

```text
study_family_id
dementia_stratum
source_stage_label
normalized_stage
insulin_abnormality
biological_compartment
brain_region_or_tissue
cell_type
measurement_method
evidence_directness_level
pathology_anchor
pathology_status
time_relation_to_pathology
time_relation_to_clinical_diagnosis
longitudinal_or_cross_sectional
prospective_or_retrospective
earliest_observed_stage
earliest_observed_time_before_diagnosis
progression_prediction
temporal_claim_class
temporal_confidence
systemic_diabetes_status
key_confounders
risk_of_bias
replication_status
source_reference_ids
```

### Disease-time synthesis

For each dementia, output:

```text
NORMAL -> PRECLINICAL PATHOLOGY -> PRODROMAL/MCI -> DEMENTIA -> ADVANCED
```

Overlay only directly supported insulin abnormalities. Show uncertainty ranges or stage bands. Do not place an event earlier than the evidence allows.

Generate two separate temporal products:

1. **Clinical clock**: timing relative to diagnosis/stage transition.
2. **Pathology clock**: timing relative to defining molecular/vascular pathology.

This distinction is required because "5 years before diagnosis" does not mean "before disease biology began."

## Measurement-validity audit

Implement explicit tracking of assay assumptions and later validation.

Priority example: L1CAM-immunocapture studies labelled as neuron-derived extracellular vesicles. Keep the original finding, but link later methodological validation and record whether the assumed neuronal-EV specificity remains supported.

Fields:

- assay/platform
- biological-specificity assumption
- original use
- later validation/invalidation
- effect on evidentiary confidence
- independent-method replication

Do not delete questionable studies; downgrade and explain.

## Recursive citation graph and pruning

The canonical data structure must be a directed graph, not a literal tree, because a reference can have multiple discovery parents.

Node states:

- included
- excluded
- duplicate
- unresolved
- inaccessible
- blocked
- registry_unpublished

Edge fields:

- source_reference_id
- target_reference_id
- discovery_route
- cycle_id
- query_id

Render a dendrogram-like left-to-right generation projection for human review, but preserve the full directed graph in GraphML/CSV.

Pruning rules:

- prune duplicate study-family expansion unless another distinct branch remains informative;
- prune ineligible branches but retain node/reason/token cost;
- never prune a pivotal contradiction solely for high risk of bias;
- merge repeated visual routes while retaining all underlying edges.

## Search cycles and temporal branch allocation

Run:

- Cycle 0: protocol validation, terminology, sentinel studies, temporal anchors.
- Cycle 1: broad direct brain-insulin and cross-dementia acquisition.
- Cycle 2: validity, replication, registry/protocol, missing evidence, assay audit.
- Cycle 3: cross-dementia model comparison plus temporal ordering analysis.
- Cycle 4+: targeted citation and onset/pathology searches.

Initial effort allocation:

- 60% stable core/direct brain evidence
- 25% new discriminators and temporal/onset evidence
- 15% contradiction, null, replication, and measurement-validation evidence

Temporal branch expansion should be triggered by:

- a newly identified earlier disease stage;
- a longitudinal cohort capable of testing precedence;
- a biomarker-defined preclinical cohort;
- a new pathology anchor;
- an assay-validity challenge affecting onset claims;
- a finding that changes whether insulin dysfunction is primary versus secondary.

## Stopping rule

Minimum two recursive citation generations. Maximum six is a safety cap, not evidence of saturation.

Stop only after:

- two consecutive low-yield cycles;
- at least one of those cycles adds zero eligible study families;
- no new conclusion-changing study families;
- no new evidence classes;
- no new material contradictions;
- no meaningful model-confidence changes;
- no temporal claim upgraded/downgraded in a conclusion-changing way;
- pivotal citation chasing is complete within accessible sources;
- remaining onset uncertainties are explicitly classified;
- central blocked claims are resolved or preserved as blocked.

## Model comparison

Do not compute one opaque composite score.

Report separately for each scientific model:

- direct evidence
- internal validity
- temporality
- mechanistic coherence
- independent replication
- specificity
- external validity
- natural history
- intervention interaction
- clinical/decision utility
- missing-evidence concern
- falsifiability

Temporal evidence must be visible as its own dimension.

## Required outputs per run

Create `runs/<run_id>/` with:

```text
protocol.json
resolved_config.json
query_plan.json
search_log.csv
reference_master.csv
study_families.csv
full_text_exclusions.csv
insulin_evidence_ledger.csv
temporal_evidence_ledger.csv
disease_trajectory_matrix.csv
pathology_ordering_matrix.csv
temporal_claims_audit.csv
measurement_validity_audit.csv
claim_evidence_matrix.csv
risk_of_bias.csv
citation_nodes.csv
citation_edges.csv
citation_graph.graphml
growth_and_pruning.svg
branch_efficiency.csv
model_comparison.json
process_metrics.jsonl
cost_summary.csv
malfunction_manifest.json
final_report.md
```

The malfunction manifest must contain enough run metadata to audit failed/charged calls: run ID, timestamp, provider/model, request ID when available, operation, retry count, token usage, cost basis, error class/message, HTTP/provider status when available, and whether the failure produced usable scientific output.

## CLI

Target commands:

```bash
python -m institute_search.cli validate --config evidence-search-comparisons/config/dementia_brain_insulin_temporal_run.json
python -m institute_search.cli plan --config ... --dry-run
python -m institute_search.cli run --config ... --output runs/<run_id>
python -m institute_search.cli resume --run runs/<run_id>
python -m institute_search.cli render-graph --run runs/<run_id>
python -m institute_search.cli summarize-cost --run runs/<run_id>
```

Support resumability. A failed external call must not require restarting completed search cycles.

## Testing requirements

No live API is required for the default test suite. Use fixtures/mocks.

Mandatory tests:

1. Config rejects fewer than three scientific models.
2. Live multi-model mode rejects fewer than three model-family adapters when required.
3. Allocation percentages must sum to 100.
4. HOMA-IR alone cannot become direct brain-insulin evidence.
5. FDG-PET alone cannot become direct brain insulin resistance.
6. Cross-sectional study cannot generate `T1_direct_precedence`.
7. Earliest observed stage is stored separately from inferred biological onset.
8. A finding years before diagnosis can still be marked after molecular pathology.
9. Questioned assay validity downgrades temporal confidence without deleting the record.
10. Multiple publications from one study family count once for replication.
11. Agreement across three LLMs does not increment scientific replication.
12. Saturation cannot occur before two recursive generations.
13. Directed citation graph supports multiple parents.
14. Pruned nodes retain reason and token attribution.
15. Missing provider usage remains null rather than fabricated.
16. Cost calculation uses a supplied pricing snapshot.
17. Resume skips completed durable steps and replays only incomplete operations.

## Acceptance criteria

The implementation is ready for a pilot when:

- all tests pass offline;
- dry-run produces complete output skeletons and query provenance;
- a small fixture corpus produces a valid directed reference graph and temporal ledger;
- temporal hard rules are enforced automatically;
- directness and biological compartment cannot be silently conflated;
- study-family replication logic is separate from publication count and LLM agreement;
- process metrics and malfunction metadata are generated even when calls fail;
- no paid call is required to validate installation and configuration.

## First pilot

Run a deliberately small pilot before the full review:

- dementia strata: AD, DLB/PDD, FTD, vascular cognitive impairment/dementia
- directness: prioritize A-B evidence
- temporal focus: preclinical/prodromal versus established dementia
- max records: small configurable cap
- minimum citation generations: 2
- three model families enabled only if API credentials are present

The pilot is successful if it can correctly distinguish:

- peripheral metabolic association from direct brain insulin evidence;
- same pathway across diseases from superficially similar terminology;
- early presence from demonstrated temporal precedence;
- pre-diagnosis evidence from pre-pathology evidence;
- publication duplication from independent replication.

Do not proceed to a high-token full run until the pilot artifacts pass these checks.
