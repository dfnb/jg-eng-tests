#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

from generate_dotnet_exercises import GRADER as DOTNET_GRADER
from generate_frontend_exercises import RUN as FRONTEND_GRADER
from production_scale_definitions import BACKEND, FRONTEND

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_DOTNET_GRADER = DOTNET_GRADER.replace(
    'project = TARGET / "src" / "Challenge" / "Challenge.csproj"',
    'project = TARGET / "src" / "ProductionApp" / "ProductionApp.csproj"',
)


def clean(value: str) -> str:
    return dedent(value).strip() + "\n"


def write(path: Path, value: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(value))
    if executable:
        path.chmod(0o755)


def literal(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def criteria(item: dict) -> list[dict]:
    return [{
        "id": f"C{index:02d}",
        "level": "minimum" if index <= 3 else "intermediate" if index == 4 else "desired",
        "weight": 3 if index == 1 else 2 if index <= 4 else 1,
        "description": case[0],
    } for index, case in enumerate(item["cases"], 1)]


ENTITIES = [
    "Customer", "Organization", "Team", "UserProfile", "PurchaseOrder", "OrderLine",
    "Invoice", "Payment", "Refund", "Shipment", "Warehouse", "InventoryItem",
    "Product", "PriceRule", "Notification", "AuditRecord", "FeatureToggle",
    "RetentionRecord", "BackgroundJob", "IntegrationEvent", "ApiClient",
    "ReportDefinition", "DocumentRecord", "ApprovalStep",
]

BACKEND_BROKEN = {
    "101": '''var p=input.Split('|');var amount=decimal.Parse(p[0],CultureInfo.InvariantCulture);return amount>=1000m?"manager-approval":"approved";''',
    "102": '''var p=input.Split('|');var amount=decimal.Parse(p[0],CultureInfo.InvariantCulture);return $"credit|{amount.ToString("0.00",CultureInfo.InvariantCulture)}|{p[2].ToUpperInvariant()}";''',
    "103": '''var p=input.Split('|');return string.IsNullOrWhiteSpace(p[2])?"unset":p[2];''',
    "104": '''var p=input.Split('|');var at=long.Parse(p[0]);var values=p[1].Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split(':')).Where(x=>long.Parse(x[0])<=at).ToArray();return values.Length==0?"missing":values[^1][1];''',
    "105": '''var p=input.Split('|');var needed=int.Parse(p[0]);var candidates=p[1].Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split(':')).Select(x=>(Id:x[0],Stock:int.Parse(x[1]),Distance:int.Parse(x[2]))).Where(x=>x.Stock>=needed).OrderBy(x=>x.Distance).ToArray();return candidates.Length==0?"unavailable":candidates[0].Id;''',
    "106": '''return string.Join(',',input.Split(',',StringSplitOptions.RemoveEmptyEntries).OrderBy(x=>x.Split(':')[0]));''',
    "107": '''var p=input.Split('|');return int.Parse(p[0])>=int.Parse(p[1])?"delete":"keep";''',
    "108": '''var p=input.Split('|');return p[0]==p[1]?"valid":"invalid";''',
    "109": '''var states=input.Split(',',StringSplitOptions.RemoveEmptyEntries);return states.All(x=>x.EndsWith(":up"))?"ready":"not-ready";''',
    "110": '''var p=input.Split('|');var percent=int.Parse(p[1]);return percent>=100?"on":"off";''',
    "111": '''var p=input.Split('|');var active=int.Parse(p[0]);return active>0?$"drain:{active}":"stopped";''',
    "112": '''if(input.Split(',').Any(x=>x.StartsWith("fail:")))return"batch-error";return string.Join(',',input.Split(',',StringSplitOptions.RemoveEmptyEntries).Select((x,i)=>$"{i}:ok:{x}"));''',
    "113": '''var p=input.Split('|');return int.Parse(p[0])!=int.Parse(p[1])?$"deprecated|sunset={p[2]}":"supported";''',
    "114": '''var allowed=new HashSet<string>{"tenant","request-type","region"};var rows=input.Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split('=',2)).Where(x=>allowed.Contains(x[0])).OrderBy(x=>x[0]).Select(x=>$"{x[0]}={x[1]}");return string.Join(',',rows);''',
    "115": '''var p=input.Split('|');return int.Parse(p[1])<int.Parse(p[2])?"retry":"fail";''',
}

FRONTEND_BROKEN = {
    "116": '''const[permissions,routes]=input.split("|");const granted=permissions.split(",")[0];return routes.split(",").filter(Boolean).filter(x=>{const[r,p]=x.split("=");return !p||p===granted}).map(x=>x.split("=")[0]).join(",")''',
    "117": '''const cmds=input.split(",");let value="",undo=[];for(const c of cmds){if(c==="undo"&&undo.length)value=undo.pop();else if(c.startsWith("set:")){undo.push(value);value=c.slice(4)}}return value||"empty"''',
    "118": '''const[current,response,status]=input.split("|").map((x,i)=>i<2?Number(x):x);if(status==="conflict")return"resolve";if(status==="network")return"retry";return response<=current?"apply":"ignore"''',
    "119": '''const[saved]=input.split("|");return String(Math.max(0,Number(saved)))''',
    "120": '''const values=input.split(",").filter(Boolean).map(Number);if(!values.length)return"empty";const trend=values.at(-1)>values[0]?"up":values.at(-1)<values[0]?"down":"flat";return`${trend}|min=${values[0]}|max=${values.at(-1)}`''',
    "121": '''const[preference,effect]=input.split("|");if(preference==="reduce")return"instant";return effect==="progress"?"animated-progress":"animate"''',
    "122": '''const[locale,raw]=input.split("|");const normalized=locale==="pt-BR"?raw.trim().replaceAll(".","").replace(",","."):raw.trim();const n=Number(normalized);return Number.isFinite(n)?n.toFixed(2):"invalid"''',
    "123": '''const[ids,command]=input.split("|");const rows=ids.split(",").filter(Boolean);const[action,id]=command.split(":");if(action==="remove")return rows.filter(x=>x!==id).join(",");if(action==="add"&&!rows.includes(id))rows.push(id);return rows.join(",")''',
    "124": '''const[current,update]=input.split("|");const map=new Map(current.split(",").filter(Boolean).map(x=>x.split(":")));const[id,value]=update.split(":");if(id)map.set(id,value);return[...map].map(([k,v])=>`${k}:${v}`).join(",")''',
    "125": '''const[server,client]=input.split("|");return server===client?"hydrate":"rerender"''',
    "126": '''const[expected0,chunks]=input.split("|");const rows=chunks.split(",").filter(Boolean).map(x=>x.split(":"));if(!rows.length)return`${expected0}|wait`;return`${Number(rows.at(-1)[0])+1}|${rows.map(x=>x[1]).join("")}`''',
    "127": '''const[limit0,incoming0,entries]=input.split("|");let used=0;const rows=entries.split(",").filter(Boolean).map(x=>{const[id,size,age,pinned]=x.split(":");used+=Number(size);return{id,size:Number(size),age:Number(age),pinned:pinned==="yes"}});const evicted=[];for(const r of rows.filter(x=>!x.pinned).sort((a,b)=>a.age-b.age)){if(used+Number(incoming0)<=Number(limit0))break;used-=r.size;evicted.push(r.id)}return used+Number(incoming0)<=Number(limit0)?evicted.join(",")||"none":"quota-error"''',
    "128": '''const[secure,api,permission]=input.split("|");if(api==="yes")return"clipboard-api";return permission==="denied"?"manual":"selection-fallback"''',
    "129": '''const[page0,sections]=input.split("|");const values=sections.split(",").filter(Boolean).map(Number);if(values.some(x=>x>Number(page0)))return"oversize";return String(Math.max(1,Math.ceil(values.reduce((a,b)=>a+b,0)/Number(page0))))''',
    "130": '''const[topic]=input.split("|");return topic.startsWith("commerce.")?"accept":"foreign"''',
}


def backend_sources(item: dict, solved: bool) -> dict[str, str]:
    files: dict[str, str] = {}
    for entity in ENTITIES:
        files[f"Domain/Entities/{entity}.cs"] = f"""
        namespace ProductionApp.Domain.Entities;

        public sealed record {entity}(
            string Id,
            string TenantId,
            string Status,
            decimal Amount,
            DateTimeOffset CreatedAt,
            DateTimeOffset UpdatedAt)
        {{
            public bool IsActive => Status is "active" or "open" or "pending";
            public bool BelongsTo(string tenantId) => StringComparer.Ordinal.Equals(TenantId, tenantId);
            public bool HasIdentity(string id) => StringComparer.Ordinal.Equals(Id, id);
            public {entity} Touch(DateTimeOffset now) => this with {{ UpdatedAt = now }};
            public {entity} ChangeStatus(string status, DateTimeOffset now) => this with {{ Status = status.Trim().ToLowerInvariant(), UpdatedAt = now }};
            public {entity} ChangeAmount(decimal amount, DateTimeOffset now) => this with {{ Amount = amount, UpdatedAt = now }};
            public IReadOnlyDictionary<string, string> Tags() => new Dictionary<string, string>
            {{
                ["entity"] = "{entity.lower()}",
                ["tenant"] = TenantId,
                ["status"] = Status
            }};
            public static {entity} Create(string id, string tenantId, DateTimeOffset now) =>
                new(id.Trim(), tenantId.Trim(), "active", 0m, now, now);
        }}
        """
    for entity in ENTITIES[:12]:
        files[f"Application/Ports/I{entity}Repository.cs"] = f"""
        using ProductionApp.Domain.Entities;

        namespace ProductionApp.Application.Ports;

        public interface I{entity}Repository
        {{
            Task<{entity}?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
            Task<IReadOnlyList<{entity}>> ListAsync(string tenantId, CancellationToken cancellationToken);
            Task SaveAsync({entity} entity, CancellationToken cancellationToken);
            Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
            Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
            Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
        }}
        """
    for entity in ENTITIES[:10]:
        files[f"Application/Services/{entity}Service.cs"] = f"""
        using ProductionApp.Application.Common;
        using ProductionApp.Application.Ports;
        using ProductionApp.Domain.Entities;

        namespace ProductionApp.Application.Services;

        public sealed class {entity}Service(I{entity}Repository repository, IApplicationClock clock)
        {{
            public Task<{entity}?> FindAsync(string tenantId, string id, CancellationToken cancellationToken) =>
                repository.FindAsync(tenantId, id, cancellationToken);

            public async Task<OperationResult<{entity}>> SaveAsync({entity} entity, CancellationToken cancellationToken)
            {{
                if (string.IsNullOrWhiteSpace(entity.Id)) return OperationResult<{entity}>.Failure("id-required");
                if (string.IsNullOrWhiteSpace(entity.TenantId)) return OperationResult<{entity}>.Failure("tenant-required");
                var normalized = entity.Touch(clock.UtcNow);
                await repository.SaveAsync(normalized, cancellationToken);
                return OperationResult<{entity}>.Success(normalized);
            }}

            public async Task<IReadOnlyList<{entity}>> ActiveAsync(string tenantId, CancellationToken cancellationToken)
            {{
                var rows = await repository.ListAsync(tenantId, cancellationToken);
                return rows.Where(row => row.IsActive).OrderBy(row => row.Id, StringComparer.Ordinal).ToArray();
            }}
        }}
        """
    files.update({
        "Application/Common/OperationResult.cs": """
        namespace ProductionApp.Application.Common;
        public sealed record OperationResult<T>(bool Succeeded, T? Value, string? Error)
        {
            public static OperationResult<T> Success(T value) => new(true, value, null);
            public static OperationResult<T> Failure(string error) => new(false, default, error);
            public OperationResult<TResult> Map<TResult>(Func<T, TResult> map) =>
                Succeeded && Value is not null ? OperationResult<TResult>.Success(map(Value)) : OperationResult<TResult>.Failure(Error ?? "unknown");
        }
        """,
        "Application/Common/IApplicationClock.cs": """
        namespace ProductionApp.Application.Common;
        public interface IApplicationClock { DateTimeOffset UtcNow { get; } }
        public sealed class SystemApplicationClock : IApplicationClock { public DateTimeOffset UtcNow => DateTimeOffset.UtcNow; }
        public sealed class FixedApplicationClock(DateTimeOffset value) : IApplicationClock { public DateTimeOffset UtcNow { get; set; } = value; }
        """,
        "Application/Common/PageSlice.cs": """
        namespace ProductionApp.Application.Common;
        public sealed record PageSlice<T>(IReadOnlyList<T> Items, string? NextCursor, int Total)
        {
            public bool HasMore => NextCursor is not null;
            public static PageSlice<T> Empty() => new(Array.Empty<T>(), null, 0);
            public PageSlice<TResult> Map<TResult>(Func<T, TResult> map) => new(Items.Select(map).ToArray(), NextCursor, Total);
        }
        """,
        "Infrastructure/Observability/CorrelationContext.cs": """
        namespace ProductionApp.Infrastructure.Observability;
        public sealed record CorrelationContext(string TraceId, string TenantId, string ActorId)
        {
            public static CorrelationContext Anonymous(string traceId) => new(traceId, "public", "anonymous");
            public IReadOnlyDictionary<string, string> SafeTags() => new Dictionary<string, string>
            {
                ["trace.id"] = TraceId,
                ["tenant.id"] = TenantId,
                ["actor.id"] = ActorId
            };
        }
        """,
        "Infrastructure/Health/DependencySnapshot.cs": """
        namespace ProductionApp.Infrastructure.Health;
        public sealed record DependencySnapshot(string Name, bool Required, bool Available, TimeSpan Latency)
        {
            public string State => Available ? "up" : "down";
            public bool BlocksReadiness => Required && !Available;
            public static DependencySnapshot Up(string name, bool required) => new(name, required, true, TimeSpan.Zero);
            public static DependencySnapshot Down(string name, bool required) => new(name, required, false, TimeSpan.Zero);
        }
        """,
        "Infrastructure/Configuration/ConfigurationValue.cs": """
        namespace ProductionApp.Infrastructure.Configuration;
        public sealed record ConfigurationValue(string Key, string Value, string Source, int Priority)
        {
            public bool IsUsable => !string.IsNullOrWhiteSpace(Key) && !string.IsNullOrWhiteSpace(Value);
            public static ConfigurationValue Select(IEnumerable<ConfigurationValue> values) =>
                values.Where(x => x.IsUsable).OrderByDescending(x => x.Priority).First();
        }
        """,
        "Infrastructure/Messaging/EventEnvelope.cs": """
        namespace ProductionApp.Infrastructure.Messaging;
        public sealed record EventEnvelope(string Id, string Type, int Version, string TenantId, DateTimeOffset OccurredAt, string Payload)
        {
            public bool IsCurrent(int version) => Version == version;
            public EventEnvelope Upgrade(int version, string payload) => this with { Version = version, Payload = payload };
            public string PartitionKey() => $"{TenantId}:{Type}";
        }
        """,
        "Infrastructure/Persistence/TransactionBoundary.cs": """
        namespace ProductionApp.Infrastructure.Persistence;
        public interface ITransactionBoundary
        {
            Task BeginAsync(CancellationToken cancellationToken);
            Task CommitAsync(CancellationToken cancellationToken);
            Task RollbackAsync(CancellationToken cancellationToken);
        }
        public sealed record TransactionOutcome(bool Committed, string? Error);
        """,
        "Api/Contracts/ApiRequest.cs": """
        namespace ProductionApp.Api.Contracts;
        public sealed record ApiRequest(string Method, string Path, string TenantId, string ActorId, string Body)
        {
            public bool IsMutation => Method is "POST" or "PUT" or "PATCH" or "DELETE";
            public string RouteKey() => $"{Method.ToUpperInvariant()} {Path.ToLowerInvariant()}";
        }
        """,
        "Api/Contracts/ApiResponse.cs": """
        namespace ProductionApp.Api.Contracts;
        public sealed record ApiResponse(int Status, string Body, IReadOnlyDictionary<string, string> Headers)
        {
            public bool IsSuccess => Status is >= 200 and < 300;
            public static ApiResponse Ok(string body) => new(200, body, new Dictionary<string, string>());
            public static ApiResponse Problem(int status, string code) => new(status, code, new Dictionary<string, string>());
        }
        """,
        "Api/Middleware/RequestPolicy.cs": """
        using ProductionApp.Api.Contracts;
        namespace ProductionApp.Api.Middleware;
        public static class RequestPolicy
        {
            public static bool HasTenant(ApiRequest request) => !string.IsNullOrWhiteSpace(request.TenantId);
            public static bool HasActor(ApiRequest request) => !string.IsNullOrWhiteSpace(request.ActorId);
            public static string AuditName(ApiRequest request) => $"{request.ActorId}:{request.RouteKey()}";
        }
        """,
    })
    policy_body = item["body"] if solved else BACKEND_BROKEN[item["id"]]
    files["Application/Policies/ScenarioPolicy.cs"] = f"""
    using System.Globalization;
    using System.Security.Cryptography;
    using System.Text;

    namespace ProductionApp.Application.Policies;

    internal static class ScenarioPolicy
    {{
        internal static string Evaluate(string input)
        {{
            {policy_body}
        }}
    }}
    """
    files["PublicApi/ScenarioFacade.cs"] = """
    using ProductionApp.Application.Policies;
    namespace ProductionApp;
    public static class ScenarioFacade
    {
        public static string Execute(string input)
        {
            ArgumentNullException.ThrowIfNull(input);
            return ScenarioPolicy.Evaluate(input);
        }
    }
    """
    return files


def write_backend(item: dict) -> None:
    name = f"{item['id']}-{item['slug']}"
    root = ROOT / "exercises" / name
    project = """
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup><TargetFramework>net10.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable><TreatWarningsAsErrors>true</TreatWarningsAsErrors></PropertyGroup>
    </Project>
    """
    tests = """
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net10.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup>
      <ItemGroup><ProjectReference Include="../../src/ProductionApp/ProductionApp.csproj" /></ItemGroup>
    </Project>
    """
    grader_bridge = """
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup><TargetFramework>net10.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup>
      <ItemGroup><ProjectReference Include="../ProductionApp/ProductionApp.csproj" /></ItemGroup>
    </Project>
    """
    public = f'''using ProductionApp;
    var value = ScenarioFacade.Execute({literal(item["cases"][0][1])});
    if (value != {literal(item["cases"][0][2])}) throw new Exception($"Resultado básico inesperado: {{value}}");
    Console.WriteLine("public-tests: ok");'''
    hidden = ["using ProductionApp;", 'void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}']
    for index, (_description, input_value, expected) in enumerate(item["cases"], 1):
        hidden.append(f'Check("C{index:02d}",{literal(input_value)},{literal(expected)});')
    rows = "\n".join(f"| {c['id']} | {c['level']} | {c['weight']} | {c['description']} | `{c['id']}` |" for c in criteria(item))
    for variant, solved in (("exercise", False), ("solution", True)):
        base = root / variant
        write(base / "global.json", '{"sdk":{"version":"10.0.100","rollForward":"latestFeature"}}')
        write(base / ".gitignore", "bin/\nobj/\n.idea/\n.vscode/")
        write(base / "src/ProductionApp/ProductionApp.csproj", project)
        write(base / "src/Challenge/Challenge.csproj", grader_bridge)
        for relative, source in backend_sources(item, solved).items():
            write(base / "src/ProductionApp" / relative, source)
        write(base / "tests/PublicTests/PublicTests.csproj", tests)
        write(base / "tests/PublicTests/Program.cs", public)
        write_common_student_files(base, item, "C# e .NET 10", "src/ProductionApp", "dotnet")
        if solved:
            write(base / "SOLUTION_NOTES.md", f"# Notas da solução\n\nA referência corrige a política de {item['focus']} atrás da fachada pública, preservando as demais camadas da aplicação.")
    write(root / "EVALUATION.md", evaluation(item, "Backend", "C# e .NET 10", rows))
    write(root / "grader/run.py", PRODUCTION_DOTNET_GRADER, True)
    write(root / "grader/Program.cs", "\n".join(hidden))
    write(root / "grader/criteria.json", json.dumps({"exercise": name, "criteria": criteria(item), "staticChecks": []}, ensure_ascii=False, indent=2))


MODEL_NAMES = ["Account", "Actor", "Address", "Alert", "Attachment", "Customer", "Document", "Feature", "Invoice", "MenuItem", "Order", "Permission", "Preference", "Report", "Route", "Workspace"]


def frontend_sources(item: dict, solved: bool) -> dict[str, str]:
    files: dict[str, str] = {}
    for name in MODEL_NAMES:
        lower = name[0].lower() + name[1:]
        files[f"domain/{lower}.ts"] = f"""
        export interface {name} {{
          id: string
          tenantId: string
          label: string
          status: "active" | "inactive" | "pending"
          version: number
          updatedAt: string
          metadata: Readonly<Record<string, string>>
        }}

        export function create{name}(id: string, tenantId: string): {name} {{
          return {{ id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {{}} }}
        }}
        export function normalize{name}(value: {name}): {name} {{
          return {{ ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }}
        }}
        export function is{name}Active(value: {name}): boolean {{ return value.status === "active" }}
        export function compare{name}(left: {name}, right: {name}): number {{ return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }}
        export function merge{name}(current: {name}, patch: Partial<{name}>): {name} {{ return normalize{name}({{ ...current, ...patch, id: current.id, tenantId: current.tenantId }}) }}
        export function index{name}s(values: readonly {name}[]): ReadonlyMap<string, {name}> {{ return new Map(values.map(value => [value.id, value])) }}
        export function visible{name}s(values: readonly {name}[]): readonly {name}[] {{ return values.filter(is{name}Active).toSorted(compare{name}) }}
        """
    for name in MODEL_NAMES[:12]:
        lower = name[0].lower() + name[1:]
        files[f"services/{lower}-service.ts"] = f"""
        import {{ create{name}, normalize{name}, type {name} }} from "../domain/{lower}.ts"

        export interface {name}Transport {{
          list(tenantId: string, signal?: AbortSignal): Promise<readonly {name}[]>
          save(value: {name}, signal?: AbortSignal): Promise<{name}>
          remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
        }}

        export class {name}Service {{
          constructor(private readonly transport: {name}Transport) {{}}
          async list(tenantId: string, signal?: AbortSignal): Promise<readonly {name}[]> {{
            const rows = await this.transport.list(tenantId, signal)
            return rows.map(normalize{name}).toSorted((a, b) => a.id.localeCompare(b.id))
          }}
          async create(tenantId: string, id: string, signal?: AbortSignal): Promise<{name}> {{
            return this.transport.save(create{name}(id, tenantId), signal)
          }}
          async update(value: {name}, signal?: AbortSignal): Promise<{name}> {{
            return this.transport.save(normalize{name}(value), signal)
          }}
          async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {{
            await this.transport.remove(tenantId, id, signal)
          }}
        }}
        """
    for index, name in enumerate(["Session", "Navigation", "Notification", "Draft", "Selection", "Filter", "Layout", "Connectivity"], 1):
        files[f"state/{name.lower()}-store.ts"] = f"""
        export type {name}State = Readonly<{{ revision: number; status: string; values: readonly string[] }}>
        export type {name}Listener = (state: {name}State) => void

        export class {name}Store {{
          private state: {name}State = {{ revision: 0, status: "idle", values: [] }}
          private readonly listeners = new Set<{name}Listener>()
          snapshot(): {name}State {{ return this.state }}
          subscribe(listener: {name}Listener): () => void {{
            this.listeners.add(listener)
            listener(this.state)
            return () => this.listeners.delete(listener)
          }}
          replace(values: readonly string[]): void {{ this.publish({{ ...this.state, revision: this.state.revision + 1, values: [...values] }}) }}
          setStatus(status: string): void {{ this.publish({{ ...this.state, revision: this.state.revision + 1, status }}) }}
          clear(): void {{ this.publish({{ revision: this.state.revision + 1, status: "idle", values: [] }}) }}
          private publish(next: {name}State): void {{ this.state = next; for (const listener of this.listeners) listener(next) }}
        }}
        export const {name.lower()}StoreVersion = {index}
        """
    for index, name in enumerate(["strings", "collections", "dates", "numbers", "urls", "errors", "events", "accessibility"], 1):
        files[f"shared/{name}.ts"] = f"""
        export function normalize{index}(value: string): string {{ return value.trim().normalize("NFC") }}
        export function present{index}(value: string | null | undefined): boolean {{ return Boolean(value?.trim()) }}
        export function unique{index}(values: readonly string[]): readonly string[] {{ return [...new Set(values)] }}
        export function ordered{index}(values: readonly string[]): readonly string[] {{ return [...values].sort((a, b) => a.localeCompare(b)) }}
        export function partition{index}(values: readonly string[], predicate: (value: string) => boolean): readonly [readonly string[], readonly string[]] {{
          const yes: string[] = []
          const no: string[] = []
          for (const value of values) (predicate(value) ? yes : no).push(value)
          return [yes, no]
        }}
        export function safeRecord{index}(entries: readonly (readonly [string, string])[]): Readonly<Record<string, string>> {{ return Object.fromEntries(entries) }}
        export function clamp{index}(value: number, minimum: number, maximum: number): number {{ return Math.min(maximum, Math.max(minimum, value)) }}
        export const moduleVersion{index} = "1.0.0"
        """
    for index in range(1, 9):
        files[f"components/feature-{index}.controller.ts"] = f"""
        export interface Feature{index}View {{
          busy: boolean
          message: string
          items: readonly string[]
          selectedId: string | null
        }}
        export class Feature{index}Controller {{
          private view: Feature{index}View = {{ busy: false, message: "", items: [], selectedId: null }}
          snapshot(): Feature{index}View {{ return this.view }}
          begin(): Feature{index}View {{ return this.view = {{ ...this.view, busy: true, message: "loading" }} }}
          succeed(items: readonly string[]): Feature{index}View {{ return this.view = {{ busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null }} }}
          fail(message: string): Feature{index}View {{ return this.view = {{ ...this.view, busy: false, message }} }}
          select(id: string): Feature{index}View {{ return this.view = {{ ...this.view, selectedId: this.view.items.includes(id) ? id : null }} }}
          reset(): Feature{index}View {{ return this.view = {{ busy: false, message: "", items: [], selectedId: null }} }}
        }}
        """
    body = item["body"] if solved else FRONTEND_BROKEN[item["id"]]
    files["features/scenario/scenario-policy.ts"] = f"export function evaluateScenario(input: string): string {{ {body} }}"
    files["app/public-api.ts"] = '''import { evaluateScenario } from "../features/scenario/scenario-policy.ts"
    export function executeScenario(input: string): string {
      if (typeof input !== "string") throw new TypeError("input must be a string")
      return evaluateScenario(input)
    }'''
    framework = item["framework"]
    if framework == "react":
        files["app/App.tsx"] = '''import React, { useState } from "react"
        import { executeScenario } from "./public-api.ts"
        export function App() {
          const [input, setInput] = useState("")
          return <main><h1>Operations Console</h1><label htmlFor="scenario">Scenario input</label><input id="scenario" value={input} onChange={event => setInput(event.target.value)} /><output aria-live="polite">{executeScenario(input)}</output></main>
        }'''
    else:
        files["app/app.component.ts"] = '''import { Component } from "@angular/core"
        import { executeScenario } from "./public-api.ts"
        @Component({ selector: "app-root", standalone: true, template: `<main><h1>Operations Console</h1><label for="scenario">Scenario input</label><input id="scenario" #field (input)="output=execute(field.value)"><output aria-live="polite">{{output}}</output></main>` })
        export class AppComponent { output = ""; execute = executeScenario }'''
    return files


def frontend_lock(name: str, framework: str) -> str:
    canonical = "07-accessible-checkout" if framework == "react" else "09-slow-dashboard"
    data = json.loads((ROOT / "exercises" / canonical / "solution" / "package-lock.json").read_text())
    data["name"] = name
    data["packages"][""]["name"] = name
    return json.dumps(data, ensure_ascii=False, indent=2)


def write_frontend(item: dict) -> None:
    name = f"{item['id']}-{item['slug']}"
    root = ROOT / "exercises" / name
    deps = {"react": "19.3.0", "react-dom": "19.3.0"} if item["framework"] == "react" else {"@angular/core": "22.1.6", "@angular/forms": "22.1.6", "rxjs": "7.8.2"}
    package = {"name": name, "private": True, "version": "1.0.0", "type": "module", "scripts": {"test": "node tests/public.test.ts", "lint": "node scripts/check-source.mjs"}, "dependencies": deps, "devDependencies": {"typescript": "7.0.2"}}
    public = f'''import test from "node:test"
    import assert from "node:assert/strict"
    import {{ executeScenario }} from "../src/app/public-api.ts"
    test("public facade", () => assert.equal(executeScenario({literal(item["cases"][0][1])}), {literal(item["cases"][0][2])}))'''
    hidden = ['import test from "node:test"', 'import assert from "node:assert/strict"', 'const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")', 'function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}']
    for index, (_description, input_value, expected) in enumerate(item["cases"], 1):
        hidden.append(f"check({literal(f'C{index:02d}')},{literal(input_value)},{literal(expected)})")
    rows = "\n".join(f"| {c['id']} | {c['level']} | {c['weight']} | {c['description']} | `{c['id']}` |" for c in criteria(item))
    checker = '''import { readdirSync, statSync } from "node:fs"
    import { join } from "node:path"
    import { spawnSync } from "node:child_process"
    import { fileURLToPath } from "node:url"
    const walk = directory => readdirSync(directory).flatMap(name => { const path=join(directory,name); return statSync(path).isDirectory()?walk(path):[path] })
    const files=walk(fileURLToPath(new URL("../src",import.meta.url))).filter(path=>path.endsWith(".ts")&&!path.endsWith(".component.ts"))
    const failures=files.filter(path=>spawnSync(process.execPath,["--check",path],{stdio:"ignore"}).status!==0)
    if(failures.length){console.error(failures.join("\\n"));process.exit(1)}
    console.log(`syntax OK: ${files.length} TypeScript modules`)'''
    for variant, solved in (("exercise", False), ("solution", True)):
        base = root / variant
        write(base / "package.json", json.dumps(package, ensure_ascii=False, indent=2))
        write(base / "package-lock.json", frontend_lock(name, item["framework"]))
        write(base / ".node-version", "24.15.0")
        write(base / ".gitignore", "node_modules/\ndist/\n.coverage/")
        for relative, source in frontend_sources(item, solved).items():
            write(base / "src" / relative, source)
        write(base / "tests/public.test.ts", public)
        write(base / "scripts/check-source.mjs", checker)
        write_common_student_files(base, item, f"{item['framework'].title()} e TypeScript", "src", "node")
        if solved:
            write(base / "SOLUTION_NOTES.md", f"# Notas da solução\n\nA referência corrige {item['focus']} no módulo de feature, mantendo a fachada e os consumidores desacoplados.")
    write(root / "EVALUATION.md", evaluation(item, "Frontend", f"{item['framework'].title()} e TypeScript", rows))
    write(root / "grader/run.py", FRONTEND_GRADER, True)
    write(root / "grader/hidden.test.ts", "\n".join(hidden))
    write(root / "grader/criteria.json", json.dumps({"exercise": name, "criteria": criteria(item), "staticChecks": []}, ensure_ascii=False, indent=2))


def write_common_student_files(base: Path, item: dict, stack: str, source_root: str, runtime: str) -> None:
    acceptance = "\n".join(f"    - {description}." for description, _input, _expected in item["cases"])
    public_input = item["cases"][0][1]
    public_output = item["cases"][0][2]
    write(base / "README.md", f"""# {item['title']}

    Este repositório simula uma aplicação pequena em produção. Ele contém módulos de domínio, serviços, portas de integração, infraestrutura, estado e entrada pública. Nem todo arquivo participa diretamente do incidente: formar um mapa da base e seguir o fluxo é parte do trabalho.

    ## Produto

    {item['summary']}

    ## Stack e organização

    {stack}. O código de produção está em `{source_root}` e os testes públicos em `tests/`. As integrações externas são substituídas por contratos locais para manter a execução determinística.

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    Preserve as APIs públicas e evite mudanças amplas antes de entender o caminho usado pela fachada.
    """)
    write(base / "CHALLENGE.md", f"""# Desafio: {item['title']}

    ## Incidente ou solicitação

    {item['summary']}

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **{item['focus']}**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

    {acceptance}

    O teste público demonstra o formato mínimo: a entrada `{public_input}` produz `{public_output}`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
    """)
    if runtime == "dotnet":
        setup = '''#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        command -v dotnet >/dev/null || { echo "Instale o SDK .NET 10." >&2; exit 1; }
        dotnet restore "$root/tests/PublicTests/PublicTests.csproj" --nologo'''
        test = '''#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        dotnet run --project "$root/tests/PublicTests/PublicTests.csproj" --nologo'''
        lint = '''#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        dotnet build "$root/tests/PublicTests/PublicTests.csproj" --nologo --no-restore'''
    else:
        setup = '''#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        cd "$root"
        npm ci --ignore-scripts'''
        test = '''#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        cd "$root"
        npm test'''
        lint = '''#!/usr/bin/env bash
        set -euo pipefail
        root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        cd "$root"
        npm run lint'''
    write(base / "scripts/setup.sh", setup, True)
    write(base / "scripts/test.sh", test, True)
    write(base / "scripts/lint.sh", lint, True)
    write(base / "scripts/start.sh", test, True)


def evaluation(item: dict, area: str, stack: str, rows: str) -> str:
    return f"""# Avaliação: {item['title']}

    - **ID:** {item['id']}
    - **Área:** {area}
    - **Tecnologias:** {stack}
    - **Perfil:** pequena aplicação de produção
    - **Tempo sugerido:** 180 minutos

    ## Intenção pedagógica

    Avaliar navegação, delimitação de responsabilidade e implementação de {item['focus']}. O caminho da fachada até a política atravessa limites explícitos da aplicação; alterar arquivos não relacionados deve ser evitado.

    **Lacuna deliberada:** uma política interna contém uma implementação parcial plausível, enquanto infraestrutura, contratos, scripts e fluxos adjacentes estão prontos.

    **Armadilha:** criar uma segunda implementação fora do fluxo real, alterar a fachada para contornar a arquitetura ou confundir módulos plausíveis com arquivos que precisam ser modificados.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Teste |
    | --- | --- | ---: | --- | --- |
    {rows}

    O grader entra pela API pública. Soluções internas diferentes da referência são aceitas desde que preservem o contrato e todos os resultados observáveis.
    """


def main() -> None:
    for item in BACKEND:
        write_backend(item)
    for item in FRONTEND:
        write_frontend(item)
    print(f"Generated {len(BACKEND)} backend and {len(FRONTEND)} frontend production-scale exercises")


if __name__ == "__main__":
    main()
