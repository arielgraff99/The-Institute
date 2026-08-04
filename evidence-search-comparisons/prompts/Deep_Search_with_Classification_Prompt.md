# Deep Search with Classification — Reusable Prompt

Conduct a rigorous, iterative, auditable evidence review of the research question below. Treat my hypothesis as a proposition to test, not as established fact. Search for supporting, contradictory, null, and reframing evidence.

## Research question

**Question:** [INSERT QUESTION]

**Primary hypothesis:** [INSERT HYPOTHESIS]

**Competing hypotheses:** [INSERT OR GENERATE BEFORE SEARCHING]

**Population/setting:** [INSERT]

**Outcomes:** [INSERT]

**Time, language, geography, and source limits:** [INSERT OR “OPEN; JUSTIFY LIMITS”]

**Deliverables:** [REPORT / TABLES / CSV / REFERENCE LIBRARY / OTHER]

**NLM recursive review gate:** ENABLED. NLM means the natural-language model/process, not the US National Library of Medicine.

**Human expert review gate:** [YES/NO; IF YES, PAUSE AFTER EACH MATERIAL CYCLE]

## Mandatory method

1. Structure the question using PICO, PECO, PICOTS, SPIDER, or another justified framework. Define inclusion/exclusion criteria, pivotal outcomes, protocol version, coverage limits, and stopping rules. Separate broad discovery from confirmation: permit terminology and hypothesis expansion during discovery, then freeze eligibility criteria, primary outcomes, subgroup definitions, and appraisal rules before confirmatory synthesis. Label later hypotheses exploratory and log every amendment. Ask only for missing information that would materially change the review; otherwise state assumptions and proceed.

2. Search across all relevant evidence classes: in vitro/basic science; animal/preclinical; human mechanistic; observational; randomized and non-randomized interventional; diagnostic/prognostic; epidemiological; psychological/behavioral; sociological/qualitative or mixed-methods; systematic reviews; guidelines; registries; and authoritative sources. Also search trial registrations, protocols, regulatory assessments, dissertations/theses, conference proceedings, preprints, corrections, expressions of concern, retractions, and unpublished or ongoing studies. Verify whether registrations and preprints have corresponding publications. Do not imply that web search exhausts subscription databases.

3. Before the full search, build a sentinel set of known pivotal papers spanning evidence classes, old and current terminology, competing hypotheses, and positive, negative, and null findings. Test whether initial queries retrieve them. Revise and document the strategy whenever a sentinel is missed. For publishable or systematic work, obtain PRESS-style peer review of the principal database strategy from an information specialist; if unavailable, perform a structured self-audit and disclose this limitation.

4. Begin with several seed-query families, then recursively mine pivotal sources for backward citations, forward citations when accessible, related articles, registrations, cited methods, datasets, terminology, authors, institutions, controversies, and companion reports. Generate targeted new queries from these discoveries. Deduplicate records and link all reports from the same underlying study or overlapping cohort.

5. Run the NLM recursive-expansion gate after every cycle. The NLM process must analyze retrieved titles, abstracts, verified full text, and metadata to normalize terminology; identify synonym families, constructs, measurements, mechanisms, populations, authors, citation clusters, contradictions, and missing evidence classes; and propose new queries. For every proposed query, state which records or concepts generated it. The NLM is a discovery and classification process—not an independent human reviewer or evidence source—and may not validate its own output. Verify every NLM-generated citation and factual claim against reliable primary sources.

6. Continue until reproducible saturation: two consecutive cycles add no eligible study that changes a conclusion, evidence class, or confidence rating; most new results are duplicates or represented study families; backward and forward citation mining of pivotal studies is complete within available access; the final strategy retrieves the sentinel set or explains every miss; and remaining database, access, language, indexing, and evidence gaps are documented. Never claim “all publications” unless coverage and saturation genuinely support it.

7. Classify every source by scientific modality and study design. Never collapse mechanistic plausibility, animal findings, observational associations, and demonstrated human clinical effects into one undifferentiated grade.

8. Extract study-level facts: design, setting, sample and groups, eligibility, intervention/exposure, comparator, outcomes, follow-up, primary numerical findings, effect estimates and uncertainty, missingness, funding, conflicts, and limitations. Prefer primary results over author interpretations. For pivotal studies, use independent duplicate eligibility review and numerical extraction when human reviewers are available. Calibrate reviewers on an initial sample, record disagreements, and adjudicate them. If only one reviewer or model pass is possible, conduct a separate verification pass and disclose the limitation.

9. Apply a current, design-appropriate risk-of-bias framework, such as RoB 2, ROBINS-I, QUADAS-2, PROBAST or its current successor, AMSTAR 2/ROBIS, ROBINS-E, SYRCLE, CASP/JBI, or MMAT. Record domain judgments and rationale; do not invent aggregate scores. Use GRADE or an explicitly justified alternative only where appropriate to the evidence type.

10. Maintain four separate functions: Searcher, Synthesizer, independent Auditor, and NLM Expansion Layer. Use separate agents only when delegation is authorized and available; otherwise perform clearly labelled sequential passes. The NLM layer identifies language patterns, concepts, gaps, and queries but cannot audit itself. The Auditor verifies citations, eligibility, sample sizes, primary results, bias judgments, overstatement, retraction/correction status, cohort overlap, missing counterevidence, and NLM-generated outputs.

11. When decisive evidence is incomplete or inconsistent, stop that claim and issue:

`QUESTION_FOR_SEARCHER: <specific missing fact, inconsistency, or targeted query>`

Run the focused search, update the records, and re-audit before using the claim. Record concise questions and decisions without exposing private chain-of-thought.

12. After each NLM gate, provide: newly detected terminology and constructs; supporting, contradictory, null, and reframing evidence; missing evidence classes; unresolved inconsistencies; provenance-linked proposed queries; and an uncertainty/hallucination audit. The Searcher verifies and executes approved queries, and the Auditor checks the results. The NLM gate may expand discovery but may not silently alter frozen confirmatory criteria.

13. If the human expert gate is enabled, keep it explicitly separate from the NLM gate. Present a compact packet containing new pivotal studies and why they matter; new concepts, authors, and measures; the relationship of findings to each hypothesis; unresolved quality or access issues; proposed inclusions/exclusions; and next-search priorities. Pause for my selections, then record the decision, date, rationale, and protocol amendment. Human review guides relevance, clinical interpretation, and priorities but does not replace reproducible eligibility or appraisal.

14. Maintain continuously updated, downloadable records:

- Exact-query search log with source, filters, date, counts, and cycle
- Reference master table covering reviewed, included, rejected, duplicate, inaccessible, retracted, and superseded records
- Full-text exclusion log with one explicit reason per record
- Study-family and overlapping-cohort linkage table
- Claim–evidence matrix containing supporting and contradictory studies
- Risk-of-bias/quality table
- Audit-question and resolution log
- NLM expansion log linking every proposed query to source records and concepts
- Human expert-gate decision log
- Sentinel-paper validation table
- Evidence graph linking publications, study families, cohorts/datasets, authors, institutions, measures, interventions, hypotheses, and claims

Never erase rejected records. Distinguish eligibility exclusions from included studies whose methodological limitations lower confidence.

15. Synthesize by evidence class, population, and outcome. Separate direct evidence from inference; statistical significance from magnitude, precision, and clinical importance; and association from causation. Report convergence, heterogeneity, inconsistency, indirectness, publication-bias concerns, and evidence gaps. Give each central conclusion a confidence rating and label it as: **directly demonstrated**, **supported by convergent evidence**, **mechanistically plausible**, **exploratory inference**, or **unsupported/contradicted**.

## Final output

Lead with the answer and identify the strongest supporting and contradictory evidence. Cite sources directly beside every substantive claim. State the review type, protocol version, discovery/confirmation boundary, last search date, databases and sources actually accessed, inaccessible sources, sentinel retrieval performance, PRESS review status, protocol deviations, and limitations. Do not call the work a systematic review unless its searching, screening, appraisal, and reporting meet that standard. Attach the structured logs so another researcher can reproduce and continue the review without reconstructing context.
