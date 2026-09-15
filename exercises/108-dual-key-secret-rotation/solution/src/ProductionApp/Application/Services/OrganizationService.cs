using ProductionApp.Application.Common;
using ProductionApp.Application.Ports;
using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Services;

public sealed class OrganizationService(IOrganizationRepository repository, IApplicationClock clock)
{
    public Task<Organization?> FindAsync(string tenantId, string id, CancellationToken cancellationToken) =>
        repository.FindAsync(tenantId, id, cancellationToken);

    public async Task<OperationResult<Organization>> SaveAsync(Organization entity, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(entity.Id)) return OperationResult<Organization>.Failure("id-required");
        if (string.IsNullOrWhiteSpace(entity.TenantId)) return OperationResult<Organization>.Failure("tenant-required");
        var normalized = entity.Touch(clock.UtcNow);
        await repository.SaveAsync(normalized, cancellationToken);
        return OperationResult<Organization>.Success(normalized);
    }

    public async Task<IReadOnlyList<Organization>> ActiveAsync(string tenantId, CancellationToken cancellationToken)
    {
        var rows = await repository.ListAsync(tenantId, cancellationToken);
        return rows.Where(row => row.IsActive).OrderBy(row => row.Id, StringComparer.Ordinal).ToArray();
    }
}
