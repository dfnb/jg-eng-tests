#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run private graders against reference solutions")
    parser.add_argument("ids", nargs="*", help="Optional two-digit exercise ids")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()
    selected = set(args.ids)
    catalog = json.loads((ROOT / "catalog.json").read_text())["exercises"]
    results = []

    for item in catalog:
        if selected and item["id"] not in selected:
            continue
        name = f"{item['id']}-{item['slug']}"
        base = ROOT / "exercises" / name
        command = [sys.executable, str(base / "grader" / "run.py"), str(base / "solution")]
        try:
            completed = subprocess.run(command, capture_output=True, text=True, timeout=args.timeout)
            report = json.loads(completed.stdout.strip().splitlines()[-1]) if completed.stdout.strip() else {}
            passed = completed.returncode == 0 and report.get("minimumPassed") is True
            results.append({"exercise": name, "passed": passed, "report": report, "stderr": completed.stderr[-1000:]})
        except (subprocess.TimeoutExpired, json.JSONDecodeError) as error:
            results.append({"exercise": name, "passed": False, "error": str(error)})
        print(f"{'PASS' if results[-1]['passed'] else 'FAIL'} {name}", file=sys.stderr)

    aggregate = {"passed": sum(result["passed"] for result in results), "total": len(results), "results": results}
    print(json.dumps(aggregate, ensure_ascii=False))
    return 0 if aggregate["passed"] == aggregate["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
