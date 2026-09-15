using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface IUserProfileRepository
{
    Task<UserProfile?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<UserProfile>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(UserProfile entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
