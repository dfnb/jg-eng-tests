using ProductionApp.Application.Common;
using ProductionApp.Application.Ports;
using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Services;

public sealed class OrderLineService(IOrderLineRepository repository, IApplicationClock clock)
{
    public Task<OrderLine?> FindAsync(string tenantId, string id, CancellationToken cancellationToken) =>
        repository.FindAsync(tenantId, id, cancellationToken);

    public async Task<OperationResult<OrderLine>> SaveAsync(OrderLine entity, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(entity.Id)) return OperationResult<OrderLine>.Failure("id-required");
        if (string.IsNullOrWhiteSpace(entity.TenantId)) return OperationResult<OrderLine>.Failure("tenant-required");
        var normalized = entity.Touch(clock.UtcNow);
        await repository.SaveAsync(normalized, cancellationToken);
        return OperationResult<OrderLine>.Success(normalized);
    }

    public async Task<IReadOnlyList<OrderLine>> ActiveAsync(string tenantId, CancellationToken cancellationToken)
    {
        var rows = await repository.ListAsync(tenantId, cancellationToken);
        return rows.Where(row => row.IsActive).OrderBy(row => row.Id, StringComparer.Ordinal).ToArray();
    }
}
