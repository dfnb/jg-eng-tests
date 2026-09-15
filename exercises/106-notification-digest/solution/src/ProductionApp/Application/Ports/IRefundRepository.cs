using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IRefundRepository
{
    Task<Refund?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Refund>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Refund entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
