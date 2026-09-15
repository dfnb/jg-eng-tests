using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IOrganizationRepository
{
    Task<Organization?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Organization>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Organization entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
