from pathlib import Path
import csv
import tempfile

from citation_flow_dendrogram import aggregate_rounds, read_records


def test_aggregation() -> None:
    rows = [
        [1, "A", "F1", "", "PROMOTED_TRACK_B", "valid", "true"],
        [1, "B", "F2", "", "DUPLICATE_CITATION", "duplicate", "false"],
        [2, "C", "F3", "A", "RETAINED_TRACK_A", "eligible", "false"],
        [2, "D", "F4", "A", "FULL_TEXT_EXCLUDED", "wrong population", "false"],
        [3, "E", "F5", "C", "PROMOTED_TRACK_B", "replicated", "false"],
    ]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "input.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow([
                "round", "citation_id", "study_family_id", "parent_citation_id",
                "validation_status", "validation_reason", "conclusion_change"
            ])
            writer.writerows(rows)
        metrics = aggregate_rounds(read_records(path))
        assert len(metrics) == 3
        assert metrics[0].unique_citations == 2
        assert metrics[0].promoted_track_b == 1
        assert metrics[0].conclusion_changing_families == 1
        assert metrics[2].conclusion_changing_families == 0


if __name__ == "__main__":
    test_aggregation()
    print("PASS")
