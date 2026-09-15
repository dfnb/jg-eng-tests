using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IInventoryItemRepository
{
    Task<InventoryItem?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<InventoryItem>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(InventoryItem entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
