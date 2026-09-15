using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IOrderLineRepository
{
    Task<OrderLine?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<OrderLine>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(OrderLine entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
