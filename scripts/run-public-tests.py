#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def main()->int:
 parser=argparse.ArgumentParser();parser.add_argument("ids",nargs="*");parser.add_argument("--variant",choices=("exercise","solution","both"),default="both");parser.add_argument("--timeout",type=int,default=120);args=parser.parse_args()
 variants=("exercise","solution") if args.variant=="both" else (args.variant,);catalog=json.loads((ROOT/"catalog.json").read_text())["exercises"];failed=[];total=0
 for item in catalog:
  if args.ids and item["id"] not in args.ids:continue
  name=f"{item['id']}-{item['slug']}"
  for variant in variants:
   total+=1;script=ROOT/"exercises"/name/variant/"scripts/test.sh"
   try:r=subprocess.run([str(script)],cwd=script.parents[1],capture_output=True,text=True,timeout=args.timeout,env=os.environ.copy());ok=r.returncode==0
   except subprocess.TimeoutExpired as e:r=e;ok=False
   print(f"{'PASS' if ok else 'FAIL'} {name}/{variant}",flush=True)
   if not ok:failed.append({"target":f"{name}/{variant}","output":((getattr(r,'stdout','')or'')+(getattr(r,'stderr','')or''))[-2000:]})
 print(json.dumps({"passed":total-len(failed),"total":total,"failures":failed},ensure_ascii=False))
 return 1 if failed else 0
if __name__=="__main__":raise SystemExit(main())
