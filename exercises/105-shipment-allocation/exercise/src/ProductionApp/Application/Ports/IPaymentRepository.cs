using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IPaymentRepository
{
    Task<Payment?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Payment>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Payment entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
