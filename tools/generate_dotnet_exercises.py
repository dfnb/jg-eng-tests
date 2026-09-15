#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
CATALOG = {x["id"]: x for x in json.loads((ROOT / "catalog.json").read_text())["exercises"]}


def clean(text: str) -> str:
    return dedent(text).strip() + "\n"


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(content))
    if executable:
        path.chmod(0o755)


def criteria_rows(criteria: list[tuple[str, str, int, str]]) -> str:
    return "\n".join(f"| {cid} | {level} | {weight} | {description} | teste privado `{cid}` |" for cid, level, weight, description in criteria)


GRADER = r'''
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
'''


def dotnet_case(case: dict) -> None:
    item = CATALOG[case["id"]]
    name = f"{item['id']}-{item['slug']}"
    root = ROOT / "exercises" / name
    criteria = case["criteria"]
    project = '''
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup>
        <TargetFramework>net10.0</TargetFramework>
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>
        <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
      </PropertyGroup>
    </Project>
    '''
    test_project = '''
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net10.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup>
      <ItemGroup><ProjectReference Include="../../src/Challenge/Challenge.csproj" /></ItemGroup>
    </Project>
    '''
    setup = '''
    #!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    command -v dotnet >/dev/null || { echo "Instale o SDK .NET 10." >&2; exit 1; }
    dotnet restore "$root/tests/PublicTests/PublicTests.csproj" --nologo
    '''
    test = '''
    #!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    dotnet run --project "$root/tests/PublicTests/PublicTests.csproj" --nologo
    '''
    lint = '''
    #!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    dotnet build "$root/tests/PublicTests/PublicTests.csproj" --nologo --no-restore
    '''
    start = '''
    #!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    echo "Executando o componente de domínio pelo host local de demonstração..."
    dotnet run --project "$root/tests/PublicTests/PublicTests.csproj" --nologo
    '''
    readme = f'''
    # {item['title']}

    Este repositório simula {case['context']}

    ## Arquitetura

    A regra avaliada fica em `src/Challenge`. `tests/PublicTests` contém somente testes básicos do contrato; a avaliação usa casos adicionais. Não altere assinaturas públicas sem necessidade.

    ## Pré-requisitos

    - SDK .NET 10
    - Bash para os atalhos em `scripts/`

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    O projeto não usa serviços pagos, credenciais nem acesso à internet durante os testes.
    '''
    challenge = f'''
    # Desafio: {item['title']}

    ## Situação

    {case['situation']}

    ## Resultado esperado

    {case['expected']}

    ## Restrições

    Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

    ## Fora de escopo

    Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

    ## Verificação e entrega

    Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
    '''
    evaluation = f'''
    # Avaliação: {item['title']}

    - **ID:** {item['id']}
    - **Tipo:** {item['kind']}
    - **Nível:** {item['level']}
    - **Duração:** {item['minutes']} minutos
    - **Tecnologias:** {', '.join(item['stack'])}

    ## Intenção e estado inicial

    {case['intent']}

    **Causa/omissão deliberada:** {case['cause']}

    **Armadilha principal:** {case['trap']}

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    {criteria_rows(criteria)}

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
    '''
    for variant, source in (("exercise", case["broken"]), ("solution", case["solution"])):
        base = root / variant
        write(base / "global.json", '{"sdk":{"version":"10.0.100","rollForward":"latestFeature"}}')
        write(base / ".gitignore", "bin/\nobj/\n*.user\n.idea/\n.vscode/\n")
        write(base / "src/Challenge/Challenge.csproj", project)
        write(base / "src/Challenge/Challenge.cs", source)
        write(base / "tests/PublicTests/PublicTests.csproj", test_project)
        write(base / "tests/PublicTests/Program.cs", case["public"])
        write(base / "scripts/setup.sh", setup, True)
        write(base / "scripts/test.sh", test, True)
        write(base / "scripts/lint.sh", lint, True)
        write(base / "scripts/start.sh", start, True)
        write(base / "README.md", readme)
        write(base / "CHALLENGE.md", challenge)
        if variant == "solution":
            write(base / "SOLUTION_NOTES.md", f"# Notas da solução\n\n{case['notes']}\n")
    write(root / "EVALUATION.md", evaluation)
    write(root / "grader/run.py", GRADER, True)
    write(root / "grader/Program.cs", case["hidden"])
    spec = {"exercise": name, "criteria": [{"id": c[0], "level": {"mínimo":"minimum","intermediário":"intermediate","desejado":"desired"}[c[1]], "weight": c[2], "description": c[3]} for c in criteria], "staticChecks": case.get("static", [])}
    write(root / "grader/criteria.json", json.dumps(spec, ensure_ascii=False, indent=2))


CASES = [
{
"id":"01","context":"a API de pedidos da loja Northstar. A aplicação já calcula subtotal e imposto; uma regra de fidelidade foi solicitada.",
"situation":"Clientes Silver recebem 5% e clientes Gold 10% de desconto sobre o subtotal antes do imposto. Bronze e níveis desconhecidos não recebem desconto.",
"expected":"Implemente a regra com arredondamento monetário para duas casas, `MidpointRounding.AwayFromZero`, sem confiar em percentuais vindos do cliente.",
"intent":"Distinguir implementação de feature orientada por regra, cuidado com dinheiro e preservação de comportamento.","cause":"o método ignora o nível de fidelidade.","trap":"aplicar desconto depois do imposto ou arredondar cedo demais.","notes":"A referência centraliza a taxa por nível, desconta o subtotal e somente então calcula imposto e arredonda o total.",
"criteria":[("C01","mínimo",3,"Gold recebe 10%"),("C02","mínimo",3,"Silver recebe 5%"),("C03","mínimo",2,"desconto precede imposto"),("C04","intermediário",1,"nível desconhecido não desconta"),("C05","desejado",1,"arredondamento de meio centavo segue a política")],
"broken":'''namespace Challenge;
public record OrderLine(decimal UnitPrice, int Quantity);
public static class Pricing {
 public static decimal Total(string level, IEnumerable<OrderLine> lines, decimal taxRate) {
  var subtotal=lines.Sum(x=>x.UnitPrice*x.Quantity);
  return Math.Round(subtotal*(1+taxRate),2,MidpointRounding.AwayFromZero);
 }
}''',
"solution":'''namespace Challenge;
public record OrderLine(decimal UnitPrice, int Quantity);
public static class Pricing {
 public static decimal Total(string level, IEnumerable<OrderLine> lines, decimal taxRate) {
  var subtotal=lines.Sum(x=>x.UnitPrice*x.Quantity);
  var rate=level.ToUpperInvariant() switch { "GOLD"=>.10m, "SILVER"=>.05m, _=>0m };
  return Math.Round(subtotal*(1-rate)*(1+taxRate),2,MidpointRounding.AwayFromZero);
 }
}''',
"public":'''using Challenge;
if(Pricing.Total("Bronze",[new(10m,2)],.1m)!=22m) throw new Exception("baseline");
Console.WriteLine("Public tests passed");''',
"hidden":'''using Challenge;
void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
C("C01",()=>Pricing.Total("Gold",[new(100m,1)],0m)==90m);
C("C02",()=>Pricing.Total("silver",[new(100m,1)],0m)==95m);
C("C03",()=>Pricing.Total("Gold",[new(100m,1)],.10m)==99m);
C("C04",()=>Pricing.Total("Platinum",[new(10m,1)],0m)==10m);
C("C05",()=>Pricing.Total("Gold",[new(.05m,1)],0m)==.05m);'''
},
{
"id":"02","context":"o serviço de reservas de um centro de distribuição, com um repositório compartilhado que representa a persistência.",
"situation":"Cancelar uma reserva ativa deve devolver o estoque uma única vez. Hoje o estado da reserva muda, mas o saldo continua reduzido.",
"expected":"Corrija a transição mantendo reserva, cancelamento e repetição consistentes, inclusive quando chamadas concorrentes chegam para a mesma reserva.",
"intent":"Avaliar diagnóstico de transição de estado, idempotência e atomicidade.","cause":"o cancelamento não devolve a quantidade e não protege a operação composta.","trap":"incrementar em todo cancelamento e permitir devolução dupla.","notes":"A referência serializa operações sobre o estado compartilhado e só devolve estoque na primeira transição Active→Cancelled.",
"criteria":[("C01","mínimo",3,"primeiro cancelamento devolve saldo"),("C02","mínimo",3,"cancelamento repetido não duplica saldo"),("C03","mínimo",2,"reserva ativa reduz saldo"),("C04","intermediário",1,"estoque insuficiente não cria reserva"),("C05","desejado",1,"cancelamentos concorrentes devolvem uma vez")],
"broken":'''namespace Challenge;
public sealed class Inventory { public int Available; public Dictionary<string,(int Qty,string State)> Reservations=new(); }
public sealed class ReservationService(Inventory data) {
 public bool Reserve(string id,int qty){ if(qty<=0||data.Available<qty)return false; data.Available-=qty; data.Reservations[id]=(qty,"Active"); return true; }
 public bool Cancel(string id){ if(!data.Reservations.TryGetValue(id,out var r))return false; data.Reservations[id]=(r.Qty,"Cancelled"); return true; }
}''',
"solution":'''namespace Challenge;
public sealed class Inventory { public int Available; public Dictionary<string,(int Qty,string State)> Reservations=new(); internal object Gate=new(); }
public sealed class ReservationService(Inventory data) {
 public bool Reserve(string id,int qty){lock(data.Gate){if(qty<=0||data.Available<qty||data.Reservations.ContainsKey(id))return false;data.Available-=qty;data.Reservations[id]=(qty,"Active");return true;}}
 public bool Cancel(string id){lock(data.Gate){if(!data.Reservations.TryGetValue(id,out var r)||r.State!="Active")return false;data.Reservations[id]=(r.Qty,"Cancelled");data.Available+=r.Qty;return true;}}
}''',
"public":'''using Challenge; var d=new Inventory{Available=10}; var s=new ReservationService(d); if(!s.Reserve("r",3)||d.Available!=7)throw new Exception(); Console.WriteLine("Public tests passed");''',
"hidden":'''using Challenge;
void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}
C("C01",()=>{var d=new Inventory{Available=10};var s=new ReservationService(d);s.Reserve("r",3);return s.Cancel("r")&&d.Available==10;});
C("C02",()=>{var d=new Inventory{Available=10};var s=new ReservationService(d);s.Reserve("r",3);s.Cancel("r");return !s.Cancel("r")&&d.Available==10;});
C("C03",()=>{var d=new Inventory{Available=5};return new ReservationService(d).Reserve("x",5)&&d.Available==0;});
C("C04",()=>{var d=new Inventory{Available=1};return !new ReservationService(d).Reserve("x",2)&&d.Reservations.Count==0;});
C("C05",()=>{var d=new Inventory{Available=10};var s=new ReservationService(d);s.Reserve("r",3);Parallel.For(0,20,_=>s.Cancel("r"));return d.Available==10;});'''
},
{
"id":"03","context":"o endpoint de relatórios de uma plataforma de vendas. A lista recebida simula as linhas materializadas pelo repositório.",
"situation":"Produza receita e quantidade por produto em um intervalo semiaberto `[from, to)`, excluindo vendas canceladas, ordenando por receita decrescente e ID como desempate, e só então paginando.",
"expected":"Corrija a consulta preservando uma ordenação determinística e validação de paginação.",
"intent":"Avaliar semântica de agregação, limites temporais e ordem correta das operações de query.","cause":"a implementação pagina eventos antes da agregação e inclui estados inválidos.","trap":"agregar depois de `Skip/Take` ou usar limite final inclusivo.","notes":"A referência filtra, agrupa, ordena e pagina nessa ordem.",
"criteria":[("C01","mínimo",3,"canceladas são excluídas"),("C02","mínimo",2,"intervalo é semiaberto"),("C03","mínimo",2,"agregação precede paginação"),("C04","intermediário",2,"ordenação possui desempate estável"),("C05","desejado",1,"paginação inválida é rejeitada")],
"broken":'''namespace Challenge;
public record Sale(string ProductId,decimal Amount,int Quantity,DateTimeOffset At,string Status);
public record ProductTotal(string ProductId,decimal Revenue,int Quantity);
public static class Reports { public static IReadOnlyList<ProductTotal> Sales(IEnumerable<Sale> sales,DateTimeOffset from,DateTimeOffset to,int skip,int take)=>sales.Where(x=>x.At>=from&&x.At<=to).Skip(skip).Take(take).GroupBy(x=>x.ProductId).Select(g=>new ProductTotal(g.Key,g.Sum(x=>x.Amount),g.Sum(x=>x.Quantity))).OrderByDescending(x=>x.Revenue).ToList(); }''',
"solution":'''namespace Challenge;
public record Sale(string ProductId,decimal Amount,int Quantity,DateTimeOffset At,string Status);
public record ProductTotal(string ProductId,decimal Revenue,int Quantity);
public static class Reports { public static IReadOnlyList<ProductTotal> Sales(IEnumerable<Sale> sales,DateTimeOffset from,DateTimeOffset to,int skip,int take){if(skip<0||take<=0)throw new ArgumentOutOfRangeException();return sales.Where(x=>x.Status=="Completed"&&x.At>=from&&x.At<to).GroupBy(x=>x.ProductId).Select(g=>new ProductTotal(g.Key,g.Sum(x=>x.Amount),g.Sum(x=>x.Quantity))).OrderByDescending(x=>x.Revenue).ThenBy(x=>x.ProductId,StringComparer.Ordinal).Skip(skip).Take(take).ToList();} }''',
"public":'''using Challenge;var now=DateTimeOffset.UtcNow;var r=Reports.Sales([new("p",10,1,now,"Completed")],now.AddMinutes(-1),now.AddMinutes(1),0,10);if(r.Single().Revenue!=10)throw new Exception();Console.WriteLine("Public tests passed");''',
"hidden":'''using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}var t=new DateTimeOffset(2025,1,1,0,0,0,TimeSpan.Zero);
C("C01",()=>Reports.Sales([new("p",10,1,t,"Cancelled"),new("p",5,2,t,"Completed")],t,t.AddDays(1),0,10).Single() is {Revenue:5,Quantity:2});
C("C02",()=>Reports.Sales([new("a",1,1,t,"Completed"),new("b",1,1,t.AddDays(1),"Completed")],t,t.AddDays(1),0,10).Count==1);
C("C03",()=>Reports.Sales([new("a",3,1,t,"Completed"),new("a",4,1,t,"Completed"),new("b",6,1,t,"Completed")],t,t.AddDays(1),0,1).Single().ProductId=="a");
C("C04",()=>string.Join(',',Reports.Sales([new("b",1,1,t,"Completed"),new("a",1,1,t,"Completed")],t,t.AddDays(1),0,2).Select(x=>x.ProductId))=="a,b");
C("C05",()=>{try{Reports.Sales([],t,t,0,0);return false;}catch(ArgumentOutOfRangeException){return true;}});'''
},
{
"id":"04","context":"a rotina de ingestão de catálogo de parceiros. O formato é CSV com cabeçalho `sku,name,price`.",
"situation":"Leia CSV UTF-8 com campos entre aspas, valide SKU único e preço decimal invariável e produza erros com o número da linha, sem persistência parcial.",
"expected":"Implemente `CatalogImporter.Parse`; em qualquer erro, `Items` deve estar vazio e `Errors` deve listar as linhas inválidas.",
"intent":"Avaliar parsing, validação e atomicidade de manipulação de dados.","cause":"o parser usa `Split(',')`, ignora duplicidade e retorna linhas válidas mesmo com erro.","trap":"tratar apenas o fixture simples e quebrar vírgulas dentro de aspas.","notes":"A referência implementa um pequeno leitor de linha com aspas escapadas e só publica itens se não houver erros.",
"criteria":[("C01","mínimo",3,"CSV válido é convertido"),("C02","mínimo",2,"campos com vírgula e aspas são lidos"),("C03","mínimo",2,"SKU duplicado aponta a linha"),("C04","intermediário",2,"erro torna o lote atômico"),("C05","desejado",1,"preço usa cultura invariável")],
"broken":'''using System.Globalization;namespace Challenge;
public record CatalogItem(string Sku,string Name,decimal Price);public record ImportError(int Line,string Code);public record ImportResult(IReadOnlyList<CatalogItem> Items,IReadOnlyList<ImportError> Errors);
public static class CatalogImporter { public static ImportResult Parse(string csv){var items=new List<CatalogItem>();var errors=new List<ImportError>();foreach(var pair in csv.Replace("\\r","").Split('\\n').Skip(1).Select((x,i)=>(x,i:i+2))){if(string.IsNullOrWhiteSpace(pair.x))continue;var p=pair.x.Split(',');if(p.Length!=3||!decimal.TryParse(p[2],out var price))errors.Add(new(pair.i,"invalid"));else items.Add(new(p[0],p[1],price));}return new(items,errors);} }''',
"solution":'''using System.Globalization;using System.Text;namespace Challenge;
public record CatalogItem(string Sku,string Name,decimal Price);public record ImportError(int Line,string Code);public record ImportResult(IReadOnlyList<CatalogItem> Items,IReadOnlyList<ImportError> Errors);
public static class CatalogImporter { static List<string> Fields(string line){var r=new List<string>();var b=new StringBuilder();bool q=false;for(int i=0;i<line.Length;i++){var c=line[i];if(c=='\"'){if(q&&i+1<line.Length&&line[i+1]=='\"'){b.Append('\"');i++;}else q=!q;}else if(c==','&&!q){r.Add(b.ToString());b.Clear();}else b.Append(c);}r.Add(b.ToString());return r;}
 public static ImportResult Parse(string csv){var items=new List<CatalogItem>();var errors=new List<ImportError>();var seen=new HashSet<string>(StringComparer.OrdinalIgnoreCase);foreach(var pair in csv.Replace("\\r","").Split('\\n').Skip(1).Select((x,i)=>(x,i:i+2))){if(string.IsNullOrWhiteSpace(pair.x))continue;var p=Fields(pair.x);if(p.Count!=3||string.IsNullOrWhiteSpace(p[0])||!decimal.TryParse(p[2],NumberStyles.Number,CultureInfo.InvariantCulture,out var price)||price<0){errors.Add(new(pair.i,"invalid"));continue;}if(!seen.Add(p[0])){errors.Add(new(pair.i,"duplicate_sku"));continue;}items.Add(new(p[0],p[1],price));}return errors.Count==0?new(items,errors):new([],errors);} }''',
"public":'''using Challenge;var r=CatalogImporter.Parse("sku,name,price\\nA,Apple,1.50");if(r.Items.Single().Price!=1.5m)throw new Exception();Console.WriteLine("Public tests passed");''',
"hidden":'''using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}var q=(char)34;var quoted=$"sku,name,price\\nA,{q}Apple, green{q},1.25\\nB,{q}Say {q}{q}hi{q}{q}{q},2";
C("C01",()=>CatalogImporter.Parse("sku,name,price\\nA,Apple,1.25").Items.Single().Name=="Apple");
C("C02",()=>CatalogImporter.Parse(quoted).Items[1].Name==$"Say {q}hi{q}");
C("C03",()=>CatalogImporter.Parse("sku,name,price\\nA,x,1\\na,y,2").Errors.Single() is {Line:3,Code:"duplicate_sku"});
C("C04",()=>CatalogImporter.Parse("sku,name,price\\nA,x,1\\nB,y,no").Items.Count==0);
C("C05",()=>CatalogImporter.Parse("sku,name,price\\nA,x,1.25").Items.Single().Price==1.25m);'''
},
{
"id":"05","context":"o envio de alertas por canais configuráveis. Adaptadores implementam uma interface local e não acessam provedores reais.",
"situation":"Envie a mensagem por todos os canais preferidos registrados. Canal desconhecido é ignorado e falha de um canal não impede os demais.",
"expected":"Remova condicionais específicas de provedor do orquestrador e use as abstrações fornecidas para tornar novos canais registráveis.",
"intent":"Avaliar Strategy/DI, composição e isolamento de falhas.","cause":"o orquestrador reconhece apenas e-mail e interrompe na primeira exceção.","trap":"adicionar outro `if` por canal ou capturar erro ao redor do lote inteiro.","notes":"A referência indexa estratégias por nome e captura falha por envio, retornando um resultado por canal.",
"criteria":[("C01","mínimo",3,"todos os canais preferidos registrados são chamados"),("C02","mínimo",2,"canal desconhecido é ignorado"),("C03","mínimo",2,"falha é isolada por canal"),("C04","intermediário",2,"novo canal funciona sem alteração do orquestrador"),("C05","desejado",1,"resultado informa sucesso e falha por canal")],
"broken":'''namespace Challenge;public interface IChannel{string Name{get;}void Send(string user,string message);}public record Delivery(string Channel,bool Success);
public sealed class Notifier(IEnumerable<IChannel> channels){readonly List<IChannel> all=channels.ToList();public IReadOnlyList<Delivery> Send(string user,string message,IEnumerable<string> preferred){var r=new List<Delivery>();foreach(var name in preferred){if(name!="email")continue;var c=all.First(x=>x.Name=="email");c.Send(user,message);r.Add(new(name,true));}return r;}}''',
"solution":'''namespace Challenge;public interface IChannel{string Name{get;}void Send(string user,string message);}public record Delivery(string Channel,bool Success);
public sealed class Notifier(IEnumerable<IChannel> channels){readonly Dictionary<string,IChannel> all=channels.ToDictionary(x=>x.Name,StringComparer.OrdinalIgnoreCase);public IReadOnlyList<Delivery> Send(string user,string message,IEnumerable<string> preferred){var r=new List<Delivery>();foreach(var name in preferred.Distinct(StringComparer.OrdinalIgnoreCase)){if(!all.TryGetValue(name,out var c))continue;try{c.Send(user,message);r.Add(new(name,true));}catch{r.Add(new(name,false));}}return r;}}''',
"public":'''using Challenge;var c=new Fake("email");new Notifier([c]).Send("u","m",["email"]);if(c.Count!=1)throw new Exception();Console.WriteLine("Public tests passed");class Fake(string n):IChannel{public string Name=>n;public int Count;public void Send(string u,string m)=>Count++;}''',
"hidden":'''using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}};
C("C01",()=>{var a=new F("sms");var b=new F("push");new Notifier([a,b]).Send("u","m",["sms","push"]);return a.N==1&&b.N==1;});
C("C02",()=>new Notifier([]).Send("u","m",["fax"]).Count==0);
C("C03",()=>{var a=new F("bad",true);var b=new F("ok");var r=new Notifier([a,b]).Send("u","m",["bad","ok"]);return b.N==1&&r.Count==2;});
C("C04",()=>{var a=new F("carrier-pigeon");new Notifier([a]).Send("u","m",["carrier-pigeon"]);return a.N==1;});
C("C05",()=>{var a=new F("bad",true);var r=new Notifier([a]).Send("u","m",["bad"]);return !r.Single().Success;});
class F(string name,bool fail=false):IChannel{public string Name=>name;public int N;public void Send(string u,string m){N++;if(fail)throw new Exception();}}'''
},
{
"id":"06","context":"o checkout de uma loja. Estoque, pagamento e persistência já têm contratos locais substituíveis.",
"situation":"O checkout deve validar o carrinho, reservar estoque, cobrar e confirmar o pedido. Falha de pagamento libera a reserva e nunca confirma o pedido.",
"expected":"Organize a orquestração em torno das interfaces fornecidas e preserve a regra de compensação.",
"intent":"Avaliar limites arquiteturais, injeção e comportamento transacional sem exigir uma estrutura interna única.","cause":"a implementação confirma antes do pagamento e não compensa estoque.","trap":"corrigir a ordem feliz e esquecer a falha depois da reserva.","notes":"A referência valida, reserva, cobra e confirma; em falha de cobrança, libera a reserva.",
"criteria":[("C01","mínimo",3,"pedido válido é reservado, cobrado e confirmado"),("C02","mínimo",3,"falha de pagamento não confirma"),("C03","mínimo",2,"falha de pagamento libera estoque"),("C04","intermediário",1,"carrinho vazio não chama gateways"),("C05","desejado",1,"dependências são substituíveis por interfaces")],
"broken":'''namespace Challenge;public interface IStock{bool Reserve(string id);void Release(string id);}public interface IPayment{bool Charge(decimal value);}public interface IOrders{void Confirm(string id);}public record Cart(string Id,decimal Total,int Items);
public sealed class Checkout(IStock stock,IPayment payment,IOrders orders){public bool Execute(Cart cart){if(cart.Items==0)return false;if(!stock.Reserve(cart.Id))return false;orders.Confirm(cart.Id);return payment.Charge(cart.Total);}}''',
"solution":'''namespace Challenge;public interface IStock{bool Reserve(string id);void Release(string id);}public interface IPayment{bool Charge(decimal value);}public interface IOrders{void Confirm(string id);}public record Cart(string Id,decimal Total,int Items);
public sealed class Checkout(IStock stock,IPayment payment,IOrders orders){public bool Execute(Cart cart){if(cart.Items<=0||cart.Total<0)return false;if(!stock.Reserve(cart.Id))return false;if(!payment.Charge(cart.Total)){stock.Release(cart.Id);return false;}orders.Confirm(cart.Id);return true;}}''',
"public":'''using Challenge;var x=new X();if(!new Checkout(x,x,x).Execute(new("o",10,1))||x.Confirmed!=1)throw new Exception();Console.WriteLine("Public tests passed");class X:IStock,IPayment,IOrders{public int Confirmed;public bool Reserve(string x)=>true;public void Release(string x){}public bool Charge(decimal v)=>true;public void Confirm(string x)=>Confirmed++;}''',
"hidden":'''using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}
C("C01",()=>{var x=new X();return new Checkout(x,x,x).Execute(new("o",1,1))&&x.R==1&&x.P==1&&x.C==1;});
C("C02",()=>{var x=new X{Pay=false};return !new Checkout(x,x,x).Execute(new("o",1,1))&&x.C==0;});
C("C03",()=>{var x=new X{Pay=false};new Checkout(x,x,x).Execute(new("o",1,1));return x.L==1;});
C("C04",()=>{var x=new X();return !new Checkout(x,x,x).Execute(new("o",0,0))&&x.R+x.P+x.C==0;});
C("C05",()=>typeof(Checkout).GetConstructors().Single().GetParameters().All(p=>p.ParameterType.IsInterface));
class X:IStock,IPayment,IOrders{public int R,P,C,L;public bool Pay=true;public bool Reserve(string x){R++;return true;}public void Release(string x)=>L++;public bool Charge(decimal v){P++;return Pay;}public void Confirm(string x)=>C++;}'''
}
]

if __name__ == "__main__":
    for case in CASES:
        dotnet_case(case)
    print(f"Generated {len(CASES)} .NET exercises")
