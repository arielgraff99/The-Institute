#!/usr/bin/env python3
"""Generate an auditable citation-growth and validation dendrogram.

The input is one row per citation occurrence in one recursive search round. The
figure shows how citations expand between rounds and how validation prunes or
promotes them. It deliberately fails when required provenance fields are absent,
so selected-reference counts cannot be misrepresented as raw search counts.
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt

ALLOWED_STATUSES = {
    "DISCOVERED",
    "DUPLICATE_CITATION",
    "MERGED_STUDY_FAMILY",
    "TITLE_ABSTRACT_EXCLUDED",
    "FULL_TEXT_EXCLUDED",
    "UNVERIFIABLE",
    "RETAINED_TRACK_A",
    "PROMOTED_TRACK_B",
    "CLAIM_BLOCKED",
}
RETAINED_STATUSES = {"RETAINED_TRACK_A", "PROMOTED_TRACK_B", "CLAIM_BLOCKED"}
ELIGIBLE_STATUSES = RETAINED_STATUSES | {"FULL_TEXT_EXCLUDED", "UNVERIFIABLE"}
REQUIRED_COLUMNS = {
    "round",
    "citation_id",
    "study_family_id",
    "parent_citation_id",
    "validation_status",
    "validation_reason",
    "conclusion_change",
}

@dataclass(frozen=True)
class CitationRecord:
    round: int
    citation_id: str
    study_family_id: str
    parent_citation_id: str
    validation_status: str
    validation_reason: str
    conclusion_change: bool

@dataclass(frozen=True)
class RoundMetrics:
    round: int
    discovered_rows: int
    unique_citations: int
    unique_study_families: int
    eligible_citations: int
    retained_track_a: int
    promoted_track_b: int
    blocked_claims: int
    pruned_total: int
    conclusion_changing_families: int
    cumulative_retained_families: int

def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n", ""}:
        return False
    raise ValueError(f"Invalid Boolean value: {value!r}")

def read_records(path: Path) -> list[CitationRecord]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("Input CSV has no header row")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError("Missing columns: " + ", ".join(sorted(missing)))
        records: list[CitationRecord] = []
        for line_no, row in enumerate(reader, start=2):
            try:
                round_no = int(row["round"])
                if round_no < 1:
                    raise ValueError("round must be >= 1")
                status = row["validation_status"].strip().upper()
                if status not in ALLOWED_STATUSES:
                    raise ValueError(f"unsupported validation_status: {status}")
                citation_id = row["citation_id"].strip()
                family_id = row["study_family_id"].strip()
                if not citation_id or not family_id:
                    raise ValueError("citation_id and study_family_id are required")
                records.append(CitationRecord(
                    round=round_no,
                    citation_id=citation_id,
                    study_family_id=family_id,
                    parent_citation_id=row["parent_citation_id"].strip(),
                    validation_status=status,
                    validation_reason=row["validation_reason"].strip(),
                    conclusion_change=parse_bool(row["conclusion_change"]),
                ))
            except Exception as exc:
                raise ValueError(f"Invalid row {line_no}: {exc}") from exc
    if not records:
        raise ValueError("Input CSV contains no citation records")
    return records

def aggregate_rounds(records: Iterable[CitationRecord]) -> list[RoundMetrics]:
    by_round: dict[int, list[CitationRecord]] = defaultdict(list)
    for record in records:
        by_round[record.round].append(record)
    rounds = sorted(by_round)
    if rounds != list(range(rounds[0], rounds[-1] + 1)):
        raise ValueError(f"Rounds must be consecutive; found {rounds}")
    cumulative_retained_families: set[str] = set()
    metrics: list[RoundMetrics] = []
    for round_no in rounds:
        items = by_round[round_no]
        citation_status: dict[str, set[str]] = defaultdict(set)
        citation_family: dict[str, str] = {}
        for item in items:
            citation_status[item.citation_id].add(item.validation_status)
            citation_family[item.citation_id] = item.study_family_id
        unique_citations = set(citation_status)
        unique_families = {citation_family[c] for c in unique_citations}
        eligible = {c for c, statuses in citation_status.items() if statuses & ELIGIBLE_STATUSES}
        retained_a = {c for c, statuses in citation_status.items() if statuses & RETAINED_STATUSES}
        promoted_b = {c for c, statuses in citation_status.items() if "PROMOTED_TRACK_B" in statuses}
        blocked = {c for c, statuses in citation_status.items() if "CLAIM_BLOCKED" in statuses}
        pruned = unique_citations - retained_a
        changed_families = {item.study_family_id for item in items if item.conclusion_change}
        cumulative_retained_families.update(citation_family[c] for c in retained_a)
        metrics.append(RoundMetrics(
            round=round_no,
            discovered_rows=len(items),
            unique_citations=len(unique_citations),
            unique_study_families=len(unique_families),
            eligible_citations=len(eligible),
            retained_track_a=len(retained_a),
            promoted_track_b=len(promoted_b),
            blocked_claims=len(blocked),
            pruned_total=len(pruned),
            conclusion_changing_families=len(changed_families),
            cumulative_retained_families=len(cumulative_retained_families),
        ))
    return metrics

def write_metrics(metrics: list[RoundMetrics], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(RoundMetrics.__dataclass_fields__)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for metric in metrics:
            writer.writerow(metric.__dict__)

def _line_width(count: int, max_count: int) -> float:
    if max_count <= 0 or count <= 0:
        return 0.6
    return 0.8 + 7.0 * math.sqrt(count / max_count)

def plot_dendrogram(metrics: list[RoundMetrics], output: Path, title: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    max_count = max(max(m.discovered_rows, m.unique_citations, m.cumulative_retained_families) for m in metrics)
    x_step = 4.0
    y = {"discovered": 4.0, "unique": 3.0, "eligible": 2.0, "retained": 1.0, "promoted": 0.0, "pruned": -1.2}
    fig, ax = plt.subplots(figsize=(max(12, len(metrics) * 4.2), 8))
    for index, metric in enumerate(metrics):
        x = index * x_step
        stage_values = [
            ("discovered", metric.discovered_rows, "Raw citation occurrences"),
            ("unique", metric.unique_citations, "Unique citations"),
            ("eligible", metric.eligible_citations, "Eligible after screening"),
            ("retained", metric.retained_track_a, "Retained: Track A"),
            ("promoted", metric.promoted_track_b, "Promoted: Track B"),
        ]
        for (stage_a, count_a, _), (stage_b, _count_b, _) in zip(stage_values, stage_values[1:]):
            ax.plot([x, x], [y[stage_a], y[stage_b]], linewidth=_line_width(count_a, max_count), solid_capstyle="round")
        for stage, count, label in stage_values:
            ax.scatter([x], [y[stage]], s=max(35, count * 7), zorder=3)
            ax.text(x + 0.15, y[stage], f"{label}\n{count}", va="center", fontsize=9)
        ax.plot([x, x + 0.75], [y["eligible"], y["pruned"]], linewidth=_line_width(metric.pruned_total, max_count), linestyle="--")
        ax.scatter([x + 0.75], [y["pruned"]], s=max(35, metric.pruned_total * 7))
        ax.text(x + 0.9, y["pruned"], f"Pruned / merged\n{metric.pruned_total}", va="center", fontsize=9)
        ax.text(x, 5.0, f"Round {metric.round}\nConclusion-changing families: {metric.conclusion_changing_families}", ha="center", fontsize=10)
        if index < len(metrics) - 1:
            next_x = (index + 1) * x_step
            ax.plot([x, next_x], [y["retained"], y["retained"]], linewidth=_line_width(metric.cumulative_retained_families, max_count))
            ax.text((x + next_x) / 2, y["retained"] + 0.2, f"Cumulative retained families: {metric.cumulative_retained_families}", ha="center", fontsize=8)
    if len(metrics) >= 3 and all(m.conclusion_changing_families == 0 for m in metrics[-3:]):
        ax.text((len(metrics) - 1) * x_step, -2.2, "Saturation criterion met:\n3 consecutive rounds with no conclusion-changing family", ha="center", fontsize=10)
    ax.set_title(title)
    ax.set_xlim(-0.8, (len(metrics) - 1) * x_step + 2.6)
    ax.set_ylim(-2.7, 5.8)
    ax.set_yticks([])
    ax.set_xticks([i * x_step for i in range(len(metrics))])
    ax.set_xticklabels([f"Round {m.round}" for m in metrics])
    ax.set_xlabel("Recursive search round")
    ax.set_frame_on(False)
    fig.tight_layout()
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(fig)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--output", type=Path, default=Path("citation_flow_dendrogram.png"))
    parser.add_argument("--metrics", type=Path, default=Path("citation_flow_metrics.csv"))
    parser.add_argument("--title", default="Citation growth and validation across recursive search rounds")
    args = parser.parse_args()
    records = read_records(args.input_csv)
    metrics = aggregate_rounds(records)
    write_metrics(metrics, args.metrics)
    plot_dendrogram(metrics, args.output, args.title)
    print(f"Wrote {args.output}")
    print(f"Wrote {args.metrics}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
