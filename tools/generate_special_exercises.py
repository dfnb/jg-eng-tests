#!/usr/bin/env python3
from __future__ import annotations
import json, shutil
from pathlib import Path
from textwrap import dedent

ROOT=Path(__file__).resolve().parents[1]
def clean(x):return dedent(x).strip()+"\n"
def write(p,x,exe=False):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(clean(x));p.chmod(0o755 if exe else 0o644)
def common(root,title,context,challenge):
 for variant in ("exercise","solution"):
  write(root/variant/".gitignore","bin/\nobj/\nnode_modules/\n.local-state/\ndist/\n");write(root/variant/"README.md",f'''# {title}

{context}

## Executar

```bash
./scripts/setup.sh
./scripts/test.sh
```

Consulte `CHALLENGE.md` para a tarefa. O repositório não exige credenciais reais.
''');write(root/variant/"CHALLENGE.md",challenge)

def make28():
 root=ROOT/"exercises/28-development-scripts";title="Scripts de desenvolvimento";common(root,title,"Este repositório simula um serviço cuja preparação local ainda depende de passos manuais.",'''# Desafio: automatizar o ambiente local

Crie scripts Bash e PowerShell equivalentes que validem ferramentas, preparem um diretório de estado, apliquem a migration fixture uma única vez e executem verificações. Eles devem funcionar a partir de qualquer diretório, propagar falhas e nunca limpar fora do estado do projeto.

Use `PROJECT_STATE_DIR` quando definido; caso contrário, use `.local-state` na raiz. Repetir setup não pode duplicar a migration. Não instale ferramentas globalmente.
''')
 broken='''#!/usr/bin/env bash
mkdir -p .local-state
echo applied >> .local-state/migrations.log
cp fixtures/sample.json .local-state/data.json
echo ready
'''
 solution='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state="${PROJECT_STATE_DIR:-$root/.local-state}"
mkdir -p "$state"
if [[ ! -f "$state/migrations.log" ]]; then printf '%s\n' 001-initial > "$state/migrations.log"; fi
cp "$root/fixtures/sample.json" "$state/data.json"
printf '%s\n' ready
'''
 reset='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state="${PROJECT_STATE_DIR:-$root/.local-state}"
case "$state" in "$root/.local-state"|/tmp/jr-eng-*/state) ;; *) echo "Refusing unsafe state path" >&2; exit 2;; esac
find "$state" -mindepth 1 -maxdepth 1 -type f -delete 2>/dev/null || true
'''
 ps='''$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$State = if ($env:PROJECT_STATE_DIR) { $env:PROJECT_STATE_DIR } else { Join-Path $Root ".local-state" }
New-Item -ItemType Directory -Force -Path $State | Out-Null
$Migration = Join-Path $State "migrations.log"
if (-not (Test-Path $Migration)) { Set-Content -Path $Migration -Value "001-initial" }
Copy-Item (Join-Path $Root "fixtures/sample.json") (Join-Path $State "data.json") -Force
Write-Output "ready"
'''
 test='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 -m json.tool "$root/fixtures/sample.json" >/dev/null
echo "Public tests passed"
'''
 start='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$root/scripts/setup.sh"
echo "Development state is ready."
'''
 lint='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
bash -n "$root/scripts/setup.sh" "$root/scripts/reset.sh" "$root/scripts/test.sh"
'''
 for variant,setup in (("exercise",broken),("solution",solution)):
  b=root/variant;write(b/"fixtures/sample.json",'{"products":[{"id":"A","stock":3}]}');write(b/"scripts/setup.sh",setup,True);write(b/"scripts/start.sh",start,True);write(b/"scripts/test.sh",test,True);write(b/"scripts/lint.sh",lint,True);write(b/"scripts/reset.sh",reset if variant=="solution" else '#!/usr/bin/env bash\nrm -rf .local-state',True);write(b/"scripts/setup.ps1",ps if variant=="solution" else 'New-Item .local-state -ItemType Directory -Force');
 write(root/"solution/SOLUTION_NOTES.md","# Notas da solução\n\nA referência resolve a raiz pelo próprio script, respeita um diretório controlado, usa modo estrito e aplica a migration idempotentemente.")
 write(root/"EVALUATION.md",'''# Avaliação: Scripts de desenvolvimento

| ID | Nível | Peso | Condição |
| --- | --- | ---: | --- |
| C01 | mínimo | 3 | setup funciona fora da raiz |
| C02 | mínimo | 2 | segunda execução não duplica migration |
| C03 | mínimo | 2 | falhas e caminhos usam quoting/modo estrito |
| C04 | intermediário | 2 | reset recusa diretório inseguro |
| C05 | desejado | 1 | PowerShell oferece o mesmo contrato |

Armadilhas: depender de `pwd`, ignorar exit codes e usar remoção ampla. O grader executa em cópia temporária e nunca aponta a limpeza para dados reais.
''')
 write(root/"grader/run.py",r'''#!/usr/bin/env python3
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
''',True)

def make29():
 root=ROOT/"exercises/29-reproducible-local-env";common(root,"Ambiente local reproduzível","Este repositório contém API e worker .NET, PostgreSQL e Redis; a orquestração local está incompleta.",'''# Desafio: ambiente local reproduzível

Complete `compose.yaml` e os Dockerfiles para que `docker compose up --build` inicie API, worker, PostgreSQL e Redis. A API só deve iniciar após dependências saudáveis, dados devem persistir em volume nomeado, portas devem ser configuráveis e processos da aplicação não devem rodar como root.
''')
 broken='''services:
  db:
    image: postgres:18
    environment: { POSTGRES_PASSWORD: devpass }
  redis:
    image: redis:8
  api:
    build: ./api
    depends_on: [db, redis]
    ports: ["8080:8080"]
  worker:
    build: ./worker
'''
 solved='''services:
  db:
    image: postgres:18.0
    environment:
      POSTGRES_PASSWORD: devpass
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 2s
      timeout: 2s
      retries: 20
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:8.2
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 2s
      timeout: 2s
      retries: 20
  api:
    build: { context: ./api }
    user: "1654:1654"
    depends_on:
      db: { condition: service_healthy }
      redis: { condition: service_healthy }
    ports: ["${API_PORT:-8080}:8080"]
  worker:
    build: { context: ./worker }
    user: "1654:1654"
    depends_on:
      db: { condition: service_healthy }
      redis: { condition: service_healthy }
volumes:
  pgdata:
'''
 docker='''FROM mcr.microsoft.com/dotnet/sdk:10.0.100 AS build
WORKDIR /src
COPY App.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /out --no-restore
FROM mcr.microsoft.com/dotnet/aspnet:10.0.0
WORKDIR /app
COPY --from=build /out .
USER 1654
ENTRYPOINT ["dotnet","App.dll"]
'''
 csproj='<Project Sdk="Microsoft.NET.Sdk.Web"><PropertyGroup><TargetFramework>net10.0</TargetFramework></PropertyGroup></Project>'
 program='''var app=WebApplication.CreateBuilder(args).Build();app.MapGet("/health",()=>Results.Ok(new{status="ok"}));app.Run();'''
 setup='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docker compose -f "$root/compose.yaml" config --quiet
'''
 test='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$root/scripts/check-compose.py"
'''
 start='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docker compose -f "$root/compose.yaml" up --build
'''
 lint='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$root/scripts/check-compose.py"
'''
 check='''from pathlib import Path
x=(Path(__file__).parents[1]/"compose.yaml").read_text()
assert all(name+":" in x for name in ("db","redis","api","worker"))
print("Public tests passed")
'''
 for variant,compose in (("exercise",broken),("solution",solved)):
  b=root/variant;write(b/"compose.yaml",compose);write(b/"api/App.csproj",csproj);write(b/"api/Program.cs",program);write(b/"api/Dockerfile",docker if variant=="solution" else 'FROM mcr.microsoft.com/dotnet/sdk:10.0\nCOPY . /app\nWORKDIR /app\nCMD ["dotnet","run"]');write(b/"worker/App.csproj",csproj.replace('.Web',''));write(b/"worker/Program.cs",'Console.WriteLine("worker ready");');write(b/"worker/Dockerfile",docker if variant=="solution" else 'FROM mcr.microsoft.com/dotnet/sdk:10.0\nCOPY . /app\nWORKDIR /app\nCMD ["dotnet","run"]');write(b/"scripts/setup.sh",setup,True);write(b/"scripts/start.sh",start,True);write(b/"scripts/test.sh",test,True);write(b/"scripts/lint.sh",lint,True);write(b/"scripts/check-compose.py",check)
 write(root/"solution/SOLUTION_NOTES.md","# Notas da solução\n\nA referência fixa tags, usa healthchecks/readiness, volume nomeado, porta configurável e runtime não root.");write(root/"EVALUATION.md",'''# Avaliação: Ambiente local reproduzível

| ID | Nível | Peso | Condição |
| --- | --- | ---: | --- |
| C01 | mínimo | 3 | quatro serviços e imagens fixas existem |
| C02 | mínimo | 2 | API espera db e redis saudáveis |
| C03 | mínimo | 2 | PostgreSQL usa volume nomeado |
| C04 | intermediário | 2 | API e worker não rodam como root |
| C05 | desejado | 1 | porta da API é configurável |
''');write(root/"grader/run.py",static_grader("29-reproducible-local-env",[("C01","minimum",3,"postgres:18\\.0.*redis:8\\.2"),("C02","minimum",2,"condition: service_healthy"),("C03","minimum",2,"pgdata:/var/lib/postgresql/data"),("C04","intermediate",2,"user: [\"']?1654"),("C05","desired",1,"API_PORT:-8080")]),True)

def static_grader(name,criteria):
 return f'''#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
t=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent.parent/"exercise");text="\\n".join(p.read_text(errors="ignore") for p in t.rglob("*") if p.is_file());spec={criteria!r};items=[]
for cid,level,weight,pattern in spec:
 ok=re.search(pattern,text,re.S|re.I) is not None;items.append({{"id":cid,"level":level,"weight":weight,"status":"pass" if ok else "fail","points":weight if ok else 0}})
score=sum(x["points"] for x in items);out={{"exercise":{name!r},"criteria":items,"score":score,"maximum":sum(x["weight"]for x in items),"minimumPassed":all(x["status"]=="pass"for x in items if x["level"]=="minimum")}};print(json.dumps(out));raise SystemExit(0 if out["minimumPassed"] else 1)
'''

def make30():
 root=ROOT/"exercises/30-integration-pipeline";common(root,"Pipeline de integração","Este monorepo simula uma API .NET e um frontend TypeScript verificados pelo mesmo pipeline.",'''# Desafio: pipeline de integração

Corrija `.github/workflows/ci.yml`: backend e frontend devem restaurar, compilar e testar; qualquer falha deve interromper; caches devem usar os lockfiles; o artefato web só pode ser publicado depois das validações e segredos nunca devem ser impressos.
''')
 broken='''name: ci
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    continue-on-error: true
    steps:
      - uses: actions/checkout@v4
      - run: dotnet build api/App.csproj || true
      - run: echo ${{ secrets.DEPLOY_TOKEN }}
'''
 solved='''name: ci
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v5
        with: { dotnet-version: '10.0.x', cache: true, cache-dependency-path: api/packages.lock.json }
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: npm, cache-dependency-path: web/package-lock.json }
      - run: dotnet restore api/App.csproj --locked-mode
      - run: dotnet build api/App.csproj --no-restore
      - run: dotnet test api/App.csproj --no-build
      - run: npm ci
        working-directory: web
      - run: npm test
        working-directory: web
      - run: npm run build
        working-directory: web
      - uses: actions/upload-artifact@v4
        if: success()
        with: { name: web-dist, path: web/dist }
'''
 setup='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
node --check "$root/web/src/index.js"
''';test=setup+'\necho "Public tests passed"';start='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 -m http.server 4173 --directory "$root/web"
''';lint=setup
 for variant,yaml in (("exercise",broken),("solution",solved)):
  b=root/variant;write(b/".github/workflows/ci.yml",yaml);write(b/"api/App.csproj",'<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>net10.0</TargetFramework><RestorePackagesWithLockFile>true</RestorePackagesWithLockFile></PropertyGroup></Project>');write(b/"api/Service.cs",'namespace Api; public static class Service { public static int Add(int a,int b)=>a+b; }');write(b/"api/packages.lock.json",'{"version":1,"dependencies":{"net10.0":{}}}');write(b/"web/package.json",'{"name":"web","private":true,"scripts":{"test":"node --test","build":"mkdir -p dist && cp src/index.js dist/"}}');write(b/"web/package-lock.json",'{"name":"web","lockfileVersion":3,"requires":true,"packages":{"":{"name":"web"}}}');write(b/"web/src/index.js",'export const add=(a,b)=>a+b;');write(b/"web/index.test.js",'import test from"node:test";import assert from"node:assert/strict";import{add}from"./src/index.js";test("add",()=>assert.equal(add(1,2),3));');write(b/"scripts/setup.sh",setup,True);write(b/"scripts/start.sh",start,True);write(b/"scripts/test.sh",test,True);write(b/"scripts/lint.sh",lint,True)
 write(root/"solution/SOLUTION_NOTES.md","# Notas da solução\n\nA referência separa setup das ferramentas, usa lockfiles como chaves implícitas de cache, não mascara exit codes e condiciona upload ao sucesso.");write(root/"EVALUATION.md",'''# Avaliação: Pipeline de integração

| ID | Nível | Peso | Condição |
| --- | --- | ---: | --- |
| C01 | mínimo | 3 | falhas não são mascaradas |
| C02 | mínimo | 2 | backend e frontend têm build/test |
| C03 | mínimo | 2 | artefato depende de sucesso |
| C04 | intermediário | 2 | cache referencia os dois lockfiles |
| C05 | desejado | 1 | workflow não imprime secrets |
''');write(root/"grader/run.py",static_grader("30-integration-pipeline",[("C01","minimum",3,"(?s)^(?!.*continue-on-error)(?!.*\\|\\| true).*"),("C02","minimum",2,"dotnet test.*npm test"),("C03","minimum",2,"upload-artifact.*if: success\\(\\)"),("C04","intermediate",2,"packages.lock.json.*package-lock.json"),("C05","desired",1,"(?s)^(?!.*echo.*secrets\\.).*")]),True)

if __name__=="__main__":
 make28();make29();make30();print("Generated 3 special exercises")
