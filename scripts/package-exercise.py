#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Package only the student-visible repository")
    parser.add_argument("exercise", help="Exercise id or directory name, e.g. 01")
    parser.add_argument("--output", type=Path, default=ROOT / ".artifacts")
    args = parser.parse_args()

    catalog = json.loads((ROOT / "catalog.json").read_text())["exercises"]
    matches = [item for item in catalog if item["id"] == args.exercise or f"{item['id']}-{item['slug']}" == args.exercise]
    if len(matches) != 1:
        raise SystemExit(f"exercise not found or ambiguous: {args.exercise}")
    item = matches[0]
    name = f"{item['id']}-{item['slug']}"
    source = ROOT / "exercises" / name / "exercise"
    if not source.is_dir():
        raise SystemExit(f"student directory not found: {source}")

    args.output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="exercise-package-") as temp:
        staging = Path(temp) / name
        shutil.copytree(source, staging, ignore=shutil.ignore_patterns("bin", "obj", "node_modules", ".coverage"))
        archive_base = args.output / name
        archive = Path(shutil.make_archive(str(archive_base), "zip", Path(temp), name))
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(".zip.sha256")
    checksum.write_text(f"{digest}  {archive.name}\n")
    print(archive)
    print(checksum)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
