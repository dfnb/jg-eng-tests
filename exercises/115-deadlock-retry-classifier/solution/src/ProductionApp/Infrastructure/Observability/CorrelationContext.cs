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
