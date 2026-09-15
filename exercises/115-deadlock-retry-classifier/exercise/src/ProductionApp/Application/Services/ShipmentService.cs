using ProductionApp.Application.Common;
using ProductionApp.Application.Ports;
using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Services;

public sealed class ShipmentService(IShipmentRepository repository, IApplicationClock clock)
{
    public Task<Shipment?> FindAsync(string tenantId, string id, CancellationToken cancellationToken) =>
        repository.FindAsync(tenantId, id, cancellationToken);

    public async Task<OperationResult<Shipment>> SaveAsync(Shipment entity, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(entity.Id)) return OperationResult<Shipment>.Failure("id-required");
        if (string.IsNullOrWhiteSpace(entity.TenantId)) return OperationResult<Shipment>.Failure("tenant-required");
        var normalized = entity.Touch(clock.UtcNow);
        await repository.SaveAsync(normalized, cancellationToken);
        return OperationResult<Shipment>.Success(normalized);
    }

    public async Task<IReadOnlyList<Shipment>> ActiveAsync(string tenantId, CancellationToken cancellationToken)
    {
        var rows = await repository.ListAsync(tenantId, cancellationToken);
        return rows.Where(row => row.IsActive).OrderBy(row => row.Id, StringComparer.Ordinal).ToArray();
    }
}
