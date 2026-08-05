# Citation-flow dendrogram

This tool visualizes **reference growth and pruning**, not the final disease taxonomy.

## Required input

One CSV row per citation occurrence per recursive round:

- `round`: recursive search round, beginning at 1.
- `citation_id`: stable DOI, PMID, registry ID, or normalized local ID.
- `study_family_id`: shared ID for companion publications/secondary analyses from the same cohort or trial.
- `parent_citation_id`: citation that led to this record through backward/forward citation searching; blank for direct search discoveries.
- `validation_status`: one of `DISCOVERED`, `DUPLICATE_CITATION`, `MERGED_STUDY_FAMILY`, `TITLE_ABSTRACT_EXCLUDED`, `FULL_TEXT_EXCLUDED`, `UNVERIFIABLE`, `RETAINED_TRACK_A`, `PROMOTED_TRACK_B`, or `CLAIM_BLOCKED`.
- `validation_reason`: explicit reason for pruning, merging, retention, promotion, or claim blocking.
- `conclusion_change`: `true` only when the independent study family changes a class-level conclusion.

## Output semantics

For each round, the figure shows:

1. raw citation occurrences;
2. unique citations after citation-level deduplication;
3. citations surviving screening;
4. citations retained in the unrestricted evidence track;
5. citations promoted to the higher-confidence track;
6. citations pruned or merged;
7. cumulative retained independent study families entering the next round;
8. number of conclusion-changing study families.

Saturation is marked only when the final three rounds contain zero conclusion-changing study families.

## Run

```bash
python citation_flow_dendrogram.py citation_flow.csv \
  --output citation_flow_dendrogram.png \
  --metrics citation_flow_metrics.csv
```

The program fails if provenance fields are missing. This prevents a selected evidence ledger from being misrepresented as a raw search-and-validation history.
