from pathlib import Path
from adjudicator import run
ROOT=Path(__file__).resolve().parents[1]
summary=run(
 ROOT/'config/frozen_disease_splitting_framework_v0.2.json',
 ROOT/'config/depression_v1.json',
 ROOT/'runs/2026-08-04/evidence_ledger.csv',
 ROOT/'runs/2026-08-04/criterion_judgments.json',
 ROOT/'runs/2026-08-04'
)
print(summary)
