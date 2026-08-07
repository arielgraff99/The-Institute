# Executive/Working-Memory Cross-Scale Addendum

## Core principle

Use executive/working-memory function as a transdiagnostic phenotype that can be traced across human cognition, anatomy, animal models, regional tissue, cells, and molecular signaling.

Disease diagnosis is a modifier. The conserved phenotype is the anchor.

## Human phenotype

Primary subdomains:

- working-memory maintenance
- working-memory updating/manipulation
- inhibitory control
- set shifting
- cognitive flexibility
- planning
- goal maintenance
- interference control

Record attention and processing speed separately because they can confound executive-task performance.

## Anatomy

Prioritize the distributed executive/working-memory system rather than a single region:

- dorsolateral prefrontal cortex
- medial prefrontal cortex
- anterior cingulate cortex
- posterior parietal cortex
- hippocampal CA1/subiculum
- mediodorsal and reuniens thalamus
- dorsal striatum/caudate

Network-level constructs:

- frontoparietal control network
- prefrontal-hippocampal network
- prefrontal-thalamic network
- frontostriatal network
- salience/control interface

Working memory and executive function are distributed circuit properties. Do not infer that one regional abnormality alone explains the phenotype.

## Cross-species translation

Map human constructs to animal tasks by cognitive operation rather than task name.

Useful animal paradigms include:

- delayed alternation
- T/Y-maze working memory
- radial-arm working memory
- delayed nonmatch-to-sample
- attentional set shifting
- reversal learning
- response inhibition
- five-choice serial reaction-time paradigms

For each experiment specify the operation actually measured: maintenance, updating, interference control, inhibition, flexibility, or planning.

## Circuit-level experiments

Prioritize causal manipulations of the relevant circuit:

- region-specific insulin/IGF challenge
- receptor or IRS manipulation
- optogenetics
- chemogenetics
- electrophysiology
- calcium imaging
- tract/circuit tracing
- functional imaging

Particularly informative circuits are PFC-hippocampus, PFC-thalamus and frontostriatal loops.

## Regional human and animal tissue

For tissue-based evidence, record exact region and layer whenever possible.

A finding in hippocampus must not automatically be generalized to DLPFC, and a finding in frontal cortex must not automatically be generalized to the whole brain.

Separate:

- INSR and IGF1R abundance
- ligand access/delivery
- receptor activation
- IRS1 versus IRS2 signaling
- PI3K/AKT
- GSK3B
- mTOR
- FOXO
- MAPK branches

## Cell types

Resolve insulin/IGF effects by cell type whenever data allow:

- excitatory pyramidal neurons
- PV interneurons
- SST interneurons
- astrocytes
- microglia
- oligodendrocytes
- endothelial cells
- pericytes

The same signaling change can have different functional meaning in different cell types.

## Cell and organoid models

Include:

- patient-derived iPSC cortical neurons
- isogenic CRISPR knock-in/correction systems
- prefrontal cortical neurons
- inhibitory interneurons
- neuron-astrocyte cocultures
- neuron-microglia cocultures
- neurovascular/endothelial systems
- cortical organoids
- cortico-thalamic and cortico-striatal assembloids where available

Preferred causal sequence:

CONTROL GENOTYPE OR CONDITION

-> perturb disease gene/pathology/insulin pathway

-> demonstrate altered insulin/IGF response

-> demonstrate synaptic/network phenotype relevant to executive/working memory

-> reverse or rescue the perturbation

-> determine whether signaling and network phenotype recover

## Functional cellular readouts

Prefer dynamic responses over static abundance:

- insulin-stimulated INSR phosphorylation
- IGF1R response
- IRS1/IRS2 state
- PI3K/AKT response
- GSK3B/mTOR/FOXO response
- synapse density
- neurite/spine metrics
- network synchrony
- E/I balance
- gamma-related network activity
- mitochondrial function
- glucose utilization
- plasticity-related transcription

Static protein expression alone does not establish functional insulin resistance.

## Cross-scale causal chain

For each study family, attempt to position evidence on this chain:

GENETIC / INFLAMMATORY / TRAUMATIC / VASCULAR / PROTEINOPATHIC INPUT

-> insulin/IGF access and signaling state

-> cell-specific trophic/plasticity response

-> regional microcircuit function

-> distributed executive/working-memory network

-> task-level executive/working-memory performance

-> broader cognitive decline

Do not fill missing links by inference. Mark them as unresolved.

## High-information experiments

The strongest evidence would combine:

1. a known disease or genetic perturbation;
2. region-specific insulin/IGF signaling measurement;
3. cellular or microcircuit readout;
4. executive/working-memory behavior;
5. causal manipulation of the insulin/IGF pathway;
6. rescue or reversal;
7. temporal ordering.

## Required outputs

Generate:

- executive_working_memory_cross_species_matrix.csv
- anatomy_network_map.csv
- region_cell_insulin_map.csv
- animal_model_translation_matrix.csv
- cell_model_translation_matrix.csv
- cross_scale_causal_chain.csv

The Institute should use these tables to test whether insulin/IGF dysregulation is a conserved mechanism of executive/working-memory decline or merely a disease-specific correlate.
