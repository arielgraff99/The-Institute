import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT/'src/run.py')], check=True, cwd=ROOT)
s=json.load(open(ROOT/'runs/2026-08-04/run_summary.json'))
assert s['historical_framework_version']=='0.2'
assert s['tracks']['HIGHER_CONFIDENCE_EVIDENCE']['DISTINCT_DISEASE']['gate']=='NOT_SUPPORTED_AS_GLOBAL_CLASS'
assert s['tracks']['HIGHER_CONFIDENCE_EVIDENCE']['OPERATIONAL_CLINICAL_CATEGORY']['gate']=='SUPPORTED'
assert s['preferred_formulation']=='COMPOSITE_MULTIAXIAL'
print('PASS')
