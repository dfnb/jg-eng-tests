#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
t=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent.parent/"exercise");text="\n".join(p.read_text(errors="ignore") for p in t.rglob("*") if p.is_file());spec=[('C01', 'minimum', 3, '(?s)^(?!.*continue-on-error)(?!.*\\|\\| true).*'), ('C02', 'minimum', 2, 'dotnet test.*npm test'), ('C03', 'minimum', 2, 'upload-artifact.*if: success\\(\\)'), ('C04', 'intermediate', 2, 'packages.lock.json.*package-lock.json'), ('C05', 'desired', 1, '(?s)^(?!.*echo.*secrets\\.).*')];items=[]
for cid,level,weight,pattern in spec:
 ok=re.search(pattern,text,re.S|re.I) is not None;items.append({"id":cid,"level":level,"weight":weight,"status":"pass" if ok else "fail","points":weight if ok else 0})
score=sum(x["points"] for x in items);out={"exercise":'30-integration-pipeline',"criteria":items,"score":score,"maximum":sum(x["weight"]for x in items),"minimumPassed":all(x["status"]=="pass"for x in items if x["level"]=="minimum")};print(json.dumps(out));raise SystemExit(0 if out["minimumPassed"] else 1)
