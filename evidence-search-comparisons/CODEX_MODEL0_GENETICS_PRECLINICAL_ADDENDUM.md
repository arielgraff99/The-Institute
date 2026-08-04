# Codex Model 0 Addendum: Genetics, Polymorphisms, and Variant-Induced Preclinical Models

## Integration rule

Load this addendum together with:

- `config/dementia_brain_insulin_temporal_run.json`
- `config/dementia_brain_insulin_model0_genetics_addendum.json`
- `CODEX_BRAIN_INSULIN_TEMPORAL_IMPLEMENTATION.md`

Model 0 must be evaluated before Models 1-5 because it addresses inherited susceptibility and experimentally induced variant effects that may exist before clinical or pathological disease stages.

## Model 0

### Genetic susceptibility and experimentally induced variant model

Test whether inherited common variants, polygenic architecture, rare/pathogenic variants, or engineered variants alter brain insulin/IGF signaling, cellular metabolism, or susceptibility to metabolic stress across dementias.

Do not treat genotype presence as evidence that insulin resistance is present from birth. Maintain two clocks:

1. genetic susceptibility clock: genotype is constitutively present;
2. functional phenotype clock: first defensible demonstration of altered insulin signaling or insulin responsiveness.

The second clock determines biological onset of the insulin phenotype.

## Genetic evidence streams

Search and classify:

1. common polymorphisms and GWAS loci;
2. fine-mapped variants and credible sets;
3. polygenic risk scores and pathway-specific polygenic scores;
4. cross-trait and local genetic correlation;
5. rare/pathogenic variants and repeat expansions;
6. eQTL, pQTL, sQTL, TWAS, and colocalization;
7. Mendelian randomization, multivariable MR, and bidirectional MR;
8. gene-by-metabolic-exposure interactions;
9. ancestry-stratified and trans-ancestry analyses;
10. variant-to-function experiments.

Always test three directions:

- dementia genotype -> insulin-signaling phenotype;
- metabolic/insulin genotype -> dementia risk or trajectory;
- shared pleiotropic architecture -> both phenotypes without demonstrated mediation.

## Preclinical variant models

Include naturally occurring and induced models:

- patient-derived iPSC neurons, astrocytes, microglia, endothelial cells, and mixed cultures carrying natural variants;
- isogenic CRISPR knock-in of risk or pathogenic variants;
- isogenic correction/reversion of patient variants;
- gene knockout, haploinsufficiency, conditional knockout, and cell-specific manipulation;
- transgenic and knock-in animal models;
- crosses between dementia-pathology models and insulin-pathway manipulations;
- cerebral organoids, midbrain organoids, assembloids, and vascularized organoid systems where applicable;
- humanized/chimeric microglial systems;
- genotype-stratified insulin challenge or metabolic-stress experiments.

### Strongest experimental pattern

Prioritize studies that:

1. introduce a variant in an isogenic background;
2. demonstrate a functional insulin-signaling abnormality;
3. correct or revert the variant;
4. rescue the phenotype;
5. reproduce the result across independent clones or experimental systems.

This is stronger evidence than non-isogenic patient-control comparisons.

## Functional insulin phenotype requirement

A preclinical model should not be labeled insulin resistant solely because it has:

- altered gene expression;
- reduced glucose metabolism;
- mitochondrial dysfunction;
- amyloid, tau, alpha-synuclein, or TDP-43 pathology;
- inflammation;
- altered body weight or systemic glucose tolerance.

Prefer functional pathway evidence such as insulin stimulation followed by receptor/pathway response, including INSR/IRS/PI3K/AKT/GSK3beta/mTOR or validated cell-type-specific downstream readouts.

## Temporal integration

For every genotype or engineered variant, record:

- genotype/variant and zygosity;
- common vs rare/pathogenic vs engineered;
- ancestry and genetic background;
- cell type or tissue;
- age/maturation stage;
- dementia pathology background;
- whether pathology was already present when insulin dysfunction was measured;
- earliest functional insulin abnormality;
- whether the phenotype precedes proteinopathy or neurodegeneration;
- whether evidence is longitudinal or staged experimentally;
- whether correction/rescue demonstrates reversibility.

Use these temporal labels:

- `G_PREEXISTING_SUSCEPTIBILITY`: genotype predates disease by definition;
- `G_FUNCTION_PREPATHOLOGY`: functional insulin phenotype demonstrated before defining pathology;
- `G_FUNCTION_WITH_PATHOLOGY`: phenotype first demonstrated after pathology is present;
- `G_FUNCTION_POST_NEURODEGENERATION`: first demonstrated after neurodegeneration;
- `G_TEMPORAL_UNRESOLVED`: experiment cannot establish ordering.

Never convert `G_PREEXISTING_SUSCEPTIBILITY` into `G_FUNCTION_PREPATHOLOGY` without functional evidence.

## Cross-dementia seed genes and loci

Use these only as starting seeds, never as a closed list.

### Alzheimer disease

APOE, TREM2, SORL1, ABCA7, BIN1, CLU, PICALM, CD33, APP, PSEN1, PSEN2.

### Lewy body/Parkinson dementia

GBA1, SNCA, LRRK2, APOE, BIN1 and additional replicated LBD/PD loci.

### Frontotemporal dementia

C9orf72, GRN, MAPT, TBK1, VCP and additional validated FTLD genes.

### Vascular cognitive impairment

NOTCH3, HTRA1, COL4A1, COL4A2, APOE and polygenic vascular/metabolic risk loci.

### Insulin/metabolic pathway seeds

INSR, IRS1, IRS2, IGF1R, PIK3CA, PIK3R1, AKT1, AKT2, GSK3B, MTOR, TCF7L2, PPARG, FTO and additional loci identified by unbiased genetic discovery.

## Required bias audit

For human genetics assess:

- population stratification;
- ancestry transferability;
- LD and fine-mapping uncertainty;
- horizontal pleiotropy;
- weak instruments;
- sample overlap;
- winner's curse;
- multiple testing;
- post-hoc pathway selection.

For preclinical genetics assess:

- genetic background;
- clone and batch effects;
- off-target editing;
- developmental compensation;
- nonphysiological overexpression;
- species differences;
- cell-type mismatch;
- absence of an insulin challenge;
- absence of isogenic rescue.

## Required outputs

Codex must generate:

- `genetic_cross_dementia_matrix.csv`
- `variant_to_insulin_function_ledger.csv`
- `polygenic_and_cross_trait_analysis.csv`
- `mendelian_randomization_audit.csv`
- `preclinical_variant_models.csv`
- `genotype_to_phenotype_temporal_map.csv`
- `gene_celltype_pathway_network.graphml`

## Model 0 adjudication question

The final synthesis must answer:

**Does genetic evidence support a shared inherited insulin-resistance liability across dementias, disease-specific variant-to-insulin mechanisms, metabolic genetic modification of dementia, pleiotropic overlap without insulin mediation, or no reproducible genetic relationship?**

Preserve more than one answer when evidence supports mixed mechanisms.