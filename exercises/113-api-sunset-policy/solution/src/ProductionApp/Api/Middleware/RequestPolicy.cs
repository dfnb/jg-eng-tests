using ProductionApp.Api.Contracts;
namespace ProductionApp.Api.Middleware;
public static class RequestPolicy
{
    public static bool HasTenant(ApiRequest request) => !string.IsNullOrWhiteSpace(request.TenantId);
    public static bool HasActor(ApiRequest request) => !string.IsNullOrWhiteSpace(request.ActorId);
    public static string AuditName(ApiRequest request) => $"{request.ActorId}:{request.RouteKey()}";
}
