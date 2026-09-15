#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = Path(sys.argv[1] if len(sys.argv) > 1 else HERE.parent / "exercise").resolve()
SPEC = json.loads((HERE / "criteria.json").read_text())
statuses = {}
diagnostics = []

project = TARGET / "src" / "Challenge" / "Challenge.csproj"
if project.exists():
    with tempfile.TemporaryDirectory(prefix="jr-grader-") as tmp:
        tmp = Path(tmp)
        reference = str(project).replace("&", "&amp;")
        (tmp / "Grader.csproj").write_text(f'<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net10.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup><ItemGroup><ProjectReference Include="{reference}" /></ItemGroup></Project>')
        (tmp / "Program.cs").write_text((HERE / "Program.cs").read_text())
        try:
            run = subprocess.run([os.environ.get("DOTNET", "dotnet"), "run", "--project", str(tmp / "Grader.csproj"), "--nologo"], capture_output=True, text=True, timeout=120)
            diagnostics.append(run.stderr[-2000:])
            if run.returncode != 0:
                diagnostics.append(run.stdout[-4000:])
            for line in run.stdout.splitlines():
                match = re.fullmatch(r"(C\d\d)\|(pass|fail)(?:\|(.*))?", line.strip())
                if match:
                    statuses[match.group(1)] = match.group(2)
                    if match.group(3): diagnostics.append(f"{match.group(1)}: {match.group(3)}")
        except (FileNotFoundError, subprocess.TimeoutExpired) as error:
            diagnostics.append(str(error))

source = "\n".join(p.read_text(errors="ignore") for p in (TARGET / "src").rglob("*.cs")) if (TARGET / "src").exists() else ""
for check in SPEC.get("staticChecks", []):
    ok = True
    if "forbid" in check: ok = re.search(check["forbid"], source, re.MULTILINE) is None
    if "require" in check: ok = ok and re.search(check["require"], source, re.MULTILINE) is not None
    statuses[check["id"]] = "pass" if ok else "fail"

items = []
for criterion in SPEC["criteria"]:
    status = statuses.get(criterion["id"], "fail")
    items.append({**criterion, "status": status, "points": criterion["weight"] if status == "pass" else 0})
minimum = all(x["status"] == "pass" for x in items if x["level"] == "minimum")
score, maximum = sum(x["points"] for x in items), sum(x["weight"] for x in items)
report = {"exercise": SPEC["exercise"], "criteria": items, "score": score, "maximum": maximum, "minimumPassed": minimum and score * 100 >= maximum * 60, "diagnostics": [x for x in diagnostics if x]}
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["minimumPassed"] else 1)
