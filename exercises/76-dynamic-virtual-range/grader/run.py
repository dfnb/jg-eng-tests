#!/usr/bin/env python3
import json,os,re,subprocess,sys
from pathlib import Path
here=Path(__file__).resolve().parent;target=Path(sys.argv[1] if len(sys.argv)>1 else here.parent/"exercise").resolve();spec=json.loads((here/"criteria.json").read_text());env={**os.environ,"CHALLENGE_TARGET":target.as_uri()};statuses={};diag=[]
try:
 r=subprocess.run(["node",str(here/"hidden.test.ts")],capture_output=True,text=True,env=env,timeout=90)
 diag.extend([r.stderr[-2000:]] if r.stderr else [])
 for line in r.stdout.splitlines():
  m=re.search(r"(C\d\d)\|(pass|fail)(?:\|(.*))?",line)
  if m:statuses[m.group(1)]=m.group(2)
except (FileNotFoundError,subprocess.TimeoutExpired) as e:diag.append(str(e))
source="\n".join(p.read_text(errors="ignore") for p in (target/"src").rglob("*") if p.is_file())
for c in spec.get("staticChecks",[]):
 ok=not re.search(c["forbid"],source,re.M) if "forbid" in c else True
 if "require" in c:ok=ok and re.search(c["require"],source,re.M) is not None
 statuses[c["id"]]="pass" if ok else "fail"
items=[]
for c in spec["criteria"]:
 s=statuses.get(c["id"],"fail");items.append({**c,"status":s,"points":c["weight"] if s=="pass" else 0})
score=sum(x["points"] for x in items);maximum=sum(x["weight"] for x in items);minimum=all(x["status"]=="pass" for x in items if x["level"]=="minimum")
out={"exercise":spec["exercise"],"criteria":items,"score":score,"maximum":maximum,"minimumPassed":minimum and score*100>=maximum*60,"diagnostics":diag};print(json.dumps(out,ensure_ascii=False));raise SystemExit(0 if out["minimumPassed"] else 1)
