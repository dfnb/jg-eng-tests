using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IPurchaseOrderRepository
{
    Task<PurchaseOrder?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<PurchaseOrder>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(PurchaseOrder entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
