using ProductionApp.Application.Common;
using ProductionApp.Application.Ports;
using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Services;

public sealed class UserProfileService(IUserProfileRepository repository, IApplicationClock clock)
{
    public Task<UserProfile?> FindAsync(string tenantId, string id, CancellationToken cancellationToken) =>
        repository.FindAsync(tenantId, id, cancellationToken);

    public async Task<OperationResult<UserProfile>> SaveAsync(UserProfile entity, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(entity.Id)) return OperationResult<UserProfile>.Failure("id-required");
        if (string.IsNullOrWhiteSpace(entity.TenantId)) return OperationResult<UserProfile>.Failure("tenant-required");
        var normalized = entity.Touch(clock.UtcNow);
        await repository.SaveAsync(normalized, cancellationToken);
        return OperationResult<UserProfile>.Success(normalized);
    }

    public async Task<IReadOnlyList<UserProfile>> ActiveAsync(string tenantId, CancellationToken cancellationToken)
    {
        var rows = await repository.ListAsync(tenantId, cancellationToken);
        return rows.Where(row => row.IsActive).OrderBy(row => row.Id, StringComparer.Ordinal).ToArray();
    }
}
