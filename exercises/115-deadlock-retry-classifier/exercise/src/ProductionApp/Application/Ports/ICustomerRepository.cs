using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface ICustomerRepository
{
    Task<Customer?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Customer>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Customer entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
