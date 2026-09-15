using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IShipmentRepository
{
    Task<Shipment?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Shipment>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Shipment entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
