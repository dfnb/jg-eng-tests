using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IInvoiceRepository
{
    Task<Invoice?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Invoice>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Invoice entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
