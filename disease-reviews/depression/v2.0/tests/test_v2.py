import json, subprocess, sys, os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
env=os.environ.copy(); env['PYTHONPATH']=str(ROOT)
subprocess.run([sys.executable,'-m','src.run'],check=True,cwd=ROOT,env=env)
s=json.load(open(ROOT/'runs/2026-08-04/run_summary_v2.json'))
h=json.load(open(ROOT/'runs/2026-08-04/holdout_validation.json'))
assert s['module_version']=='2.0'
assert s['records']==35
assert s['tracks']['HIGHER_CONFIDENCE_EVIDENCE']['DISTINCT_DISEASE']['gate']=='NOT_SUPPORTED_AS_GLOBAL_CLASS'
assert s['tracks']['HIGHER_CONFIDENCE_EVIDENCE']['BIOLOGICAL_SUBTYPE_OR_ENDOTYPE']['gate']=='NOT_SUPPORTED_AS_GLOBAL_CLASS'
assert s['tracks']['HIGHER_CONFIDENCE_EVIDENCE']['OPERATIONAL_CLINICAL_CATEGORY']['gate']=='SUPPORTED'
assert s['preferred_formulation']=='COMPOSITE_MULTIAXIAL'
assert s['mdd_endotype_structure']=='PROVISIONALLY_SUPPORTED'
assert s['global_trd_equals_single_endotype']=='NOT_SUPPORTED'
assert h['all_promoted_scientific_criteria_retain_nonpsychiatric_support'] is True
assert s['holdout_changes_classification'] is False
print('PASS v2')
