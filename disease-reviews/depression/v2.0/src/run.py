from pathlib import Path
from .common import load_csv, write_json, write_csv
from .trajectory import analyze_trajectory
from .temporality import analyze_temporality
from .pseudoresistance import analyze_pseudoresistance
from .endotypes import analyze_endotypes
from .holdout import validate_holdout
from .adjudicator_v2 import run as adjudicate

ROOT=Path(__file__).resolve().parents[1]; RUN=ROOT/'runs/2026-08-04'
rows=load_csv(RUN/'evidence_ledger_v2.csv')
analyses={
 'trajectory':analyze_trajectory(rows),
 'temporality':analyze_temporality(rows),
 'pseudoresistance':analyze_pseudoresistance(rows),
 'endotypes':analyze_endotypes(rows),
 'holdout_validation':validate_holdout(ROOT/'config/nonpsychiatric_holdout_framework_v0.2H1.json',ROOT/'config/nonpsychiatric_holdout_support_map.json')
}
for k,v in analyses.items(): write_json(RUN/f'{k}.json',v)
write_csv(RUN/'trajectory_matrix.csv',[{k:r[k] for k in ['record_id','study_family_id','trajectory_state','timing','trd_definition']} for r in rows])
write_csv(RUN/'temporality_matrix.csv',[{k:r[k] for k in ['record_id','study_family_id','domain','temporality_role','timing','finding']} for r in rows])
write_csv(RUN/'pseudoresistance_matrix_v2.csv',[{k:r[k] for k in ['record_id','study_family_id','adequacy_verified','adherence_assessed','pseudoresistance_vulnerability','causal_alternatives']} for r in rows])
write_csv(RUN/'endotype_matrix.csv',[{k:r[k] for k in ['record_id','study_family_id','domain','endotype_scope','endotype_candidate','temporality_role','finding']} for r in rows if r['endotype_candidate']!='NONE'])
summary=adjudicate(ROOT/'config/frozen_disease_splitting_framework_v0.2.json',ROOT/'config/nonpsychiatric_holdout_framework_v0.2H1.json',ROOT/'config/depression_v2.json',RUN/'evidence_ledger_v2.csv',RUN/'criterion_judgments_v2.json',RUN,analyses)
write_json(RUN/'holdout_sensitivity_v2.json',{'validation':analyses['holdout_validation'],'full_gates':summary['tracks']['HIGHER_CONFIDENCE_EVIDENCE'],'holdout_gates':summary['nonpsychiatric_holdout_gates'],'classification_changed':summary['holdout_changes_classification']})
print(summary)
