namespace ProductionApp.Api.Contracts;
public sealed record ApiRequest(string Method, string Path, string TenantId, string ActorId, string Body)
{
    public bool IsMutation => Method is "POST" or "PUT" or "PATCH" or "DELETE";
    public string RouteKey() => $"{Method.ToUpperInvariant()} {Path.ToLowerInvariant()}";
}
