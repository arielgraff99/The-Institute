from pathlib import Path
from src.adjudicator import run

def main():
    root=Path(__file__).resolve().parent
    s=run(root)
    assert s["records"] >= 30
    assert s["preferred_formulation"] == "COMPOSITE_MULTIAXIAL"
    assert s["global_distinct_disease"] == "NOT_SUPPORTED"
    assert s["trs"] == "SUPPORTED_AS_TREATMENT_RESPONSE_STATE"
    assert "unchanged" in s["holdout_result"]
    print("PASS schizophrenia v1")

if __name__=="__main__":
    main()
