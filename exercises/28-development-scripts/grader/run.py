#!/usr/bin/env python3
import json,re,subprocess,sys,tempfile,shutil,os
from pathlib import Path
target=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent.parent/"exercise").resolve();status={}
with tempfile.TemporaryDirectory(prefix="jr-eng-28-") as t:
 copy=Path(t)/"repo";shutil.copytree(target,copy);state=Path(t)/"state";env={**os.environ,"PROJECT_STATE_DIR":str(state)}
 r=subprocess.run([str(copy/"scripts/setup.sh")],cwd="/tmp",env=env,capture_output=True,text=True);status["C01"]=r.returncode==0 and (state/"data.json").exists()
 subprocess.run([str(copy/"scripts/setup.sh")],cwd="/tmp",env=env,capture_output=True);lines=(state/"migrations.log").read_text().splitlines() if (state/"migrations.log").exists() else [];status["C02"]=lines==["001-initial"]
 text=(copy/"scripts/setup.sh").read_text();status["C03"]="set -euo pipefail" in text and '"$state"' in text
 unsafe=Path(t)/"unsafe";unsafe.mkdir();(unsafe/"keep").write_text("x");rr=subprocess.run([str(copy/"scripts/reset.sh")],env={**os.environ,"PROJECT_STATE_DIR":str(unsafe)},capture_output=True);status["C04"]=rr.returncode!=0 and (unsafe/"keep").exists()
 ps=(copy/"scripts/setup.ps1").read_text();status["C05"]="$ErrorActionPreference" in ps and "PROJECT_STATE_DIR" in ps
weights={"C01":3,"C02":2,"C03":2,"C04":2,"C05":1};levels={"C01":"minimum","C02":"minimum","C03":"minimum","C04":"intermediate","C05":"desired"};items=[{"id":k,"level":levels[k],"weight":v,"status":"pass" if status.get(k) else "fail","points":v if status.get(k) else 0}for k,v in weights.items()];score=sum(x["points"]for x in items);out={"exercise":"28-development-scripts","criteria":items,"score":score,"maximum":10,"minimumPassed":all(x["status"]=="pass"for x in items if x["level"]=="minimum")};print(json.dumps(out));raise SystemExit(0 if out["minimumPassed"] else 1)
