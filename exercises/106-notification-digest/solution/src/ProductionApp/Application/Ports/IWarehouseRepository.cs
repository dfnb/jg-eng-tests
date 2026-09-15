using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IWarehouseRepository
{
    Task<Warehouse?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Warehouse>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Warehouse entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
