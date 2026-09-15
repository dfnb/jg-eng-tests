#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = ("exercise", "solution", "grader", "EVALUATION.md")
REQUIRED_STUDENT = ("README.md", "CHALLENGE.md", "scripts/setup.sh", "scripts/start.sh", "scripts/test.sh", "scripts/lint.sh")
PRIVATE_MARKERS = ("../solution", "../grader", "EVALUATION.md", "SOLUTION_NOTES.md")


def main() -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text())
    errors: list[str] = []
    expected = {f"{item['id']}-{item['slug']}" for item in catalog["exercises"]}
    actual = {path.name for path in (ROOT / "exercises").iterdir() if path.is_dir()} if (ROOT / "exercises").exists() else set()

    for missing in sorted(expected - actual):
        errors.append(f"missing exercise directory: {missing}")
    for unexpected in sorted(actual - expected):
        errors.append(f"unexpected exercise directory: {unexpected}")

    for name in sorted(expected & actual):
        base = ROOT / "exercises" / name
        for relative in REQUIRED_ROOT:
            if not (base / relative).exists():
                errors.append(f"{name}: missing {relative}")
        for relative in REQUIRED_STUDENT:
            if not (base / "exercise" / relative).is_file():
                errors.append(f"{name}: student package missing {relative}")
            if not (base / "solution" / relative).is_file():
                errors.append(f"{name}: solution missing {relative}")
        if not (base / "solution" / "SOLUTION_NOTES.md").is_file():
            errors.append(f"{name}: solution missing SOLUTION_NOTES.md")
        if not (base / "grader" / "run.py").is_file():
            errors.append(f"{name}: grader missing run.py")
        item = next(x for x in catalog["exercises"] if f"{x['id']}-{x['slug']}" == name)
        if any(stack in item["stack"] for stack in ("react", "angular")):
            for variant in ("exercise", "solution"):
                if not (base / variant / "package-lock.json").is_file():
                    errors.append(f"{name}: {variant} missing package-lock.json")
                if not (base / variant / ".node-version").is_file():
                    errors.append(f"{name}: {variant} missing .node-version")
        student = base / "exercise"
        for path in student.rglob("*") if student.exists() else ():
            if not path.is_file() or path.stat().st_size > 2_000_000:
                continue
            try:
                text = path.read_text(errors="ignore")
            except OSError:
                continue
            for marker in PRIVATE_MARKERS:
                if marker in text:
                    errors.append(f"{name}: private marker {marker!r} in {path.relative_to(student)}")

        if item.get("codebaseProfile") == "small-production":
            for variant in ("exercise", "solution"):
                source_root = base / variant / "src"
                source_files = [
                    path for path in source_root.rglob("*")
                    if path.is_file()
                    and path.suffix in {".cs", ".ts", ".tsx"}
                    and not {"bin", "obj", "node_modules"}.intersection(path.relative_to(source_root).parts)
                ]
                nonblank_lines = sum(sum(1 for line in path.read_text(errors="ignore").splitlines() if line.strip()) for path in source_files)
                functional_directories = {path.parent.relative_to(source_root) for path in source_files}
                if len(source_files) < 40:
                    errors.append(f"{name}: {variant} small-production profile requires 40 source files, found {len(source_files)}")
                if nonblank_lines < 800:
                    errors.append(f"{name}: {variant} small-production profile requires 800 nonblank source lines, found {nonblank_lines}")
                if len(functional_directories) < 6:
                    errors.append(f"{name}: {variant} small-production profile requires 6 source directories, found {len(functional_directories)}")

    if len(catalog["exercises"]) != 130:
        errors.append(f"catalog must contain 130 exercises, found {len(catalog['exercises'])}")

    if errors:
        print("Structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Structure OK: {len(expected)} exercises")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
