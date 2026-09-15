#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def main()->int:
 parser=argparse.ArgumentParser();parser.add_argument("ids",nargs="*");args=parser.parse_args()
 catalog=json.loads((ROOT/"catalog.json").read_text())["exercises"]
 catalog=[item for item in catalog if not args.ids or item["id"] in args.ids];bad=[]
 for item in catalog:
  name=f"{item['id']}-{item['slug']}";base=ROOT/"exercises"/name
  run=subprocess.run([sys.executable,str(base/"grader/run.py"),str(base/"exercise")],capture_output=True,text=True,env=os.environ.copy(),timeout=180)
  try:report=json.loads(run.stdout.strip().splitlines()[-1]);ok=run.returncode!=0 and report.get("minimumPassed") is False and any(x["level"]=="minimum" and x["status"]=="fail" for x in report.get("criteria",[]))
  except (json.JSONDecodeError,IndexError):report={};ok=False
  print(f"{'PASS' if ok else 'FAIL'} {name}: initial state is intentionally incomplete",flush=True)
  if not ok:bad.append({"exercise":name,"returnCode":run.returncode,"report":report,"stderr":run.stderr[-1000:]})
 print(json.dumps({"passed":len(catalog)-len(bad),"total":len(catalog),"failures":bad},ensure_ascii=False))
 return 1 if bad else 0
if __name__=="__main__":raise SystemExit(main())
