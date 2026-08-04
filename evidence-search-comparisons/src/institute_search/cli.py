from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_config
from .engine import EvidenceSearchEngine


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="institute-search")
    sub = p.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("--config", required=True)
    validate.add_argument("--overlay", action="append", default=[])

    simulate = sub.add_parser("simulate")
    simulate.add_argument("--config", required=True)
    simulate.add_argument("--overlay", action="append", default=[])
    simulate.add_argument("--cycles", required=True, help="JSON array of normalized cycle payloads")
    simulate.add_argument("--output", required=True)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config(args.config, *args.overlay)

    if args.command == "validate":
        print(cfg.model_dump_json(indent=2))
        return 0

    if args.command == "simulate":
        cycles = json.loads(Path(args.cycles).read_text(encoding="utf-8"))
        engine = EvidenceSearchEngine(cfg)
        for cycle in cycles:
            audit = engine.ingest_cycle(cycle)
            print(
                f"generation={audit.generation_number} "
                f"novel={len(audit.novel_insights)} "
                f"zero_streak={engine.state.consecutive_zero_novel_insight_cycles} "
                f"status={engine.state.status}"
            )
        engine.write_run(args.output)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
