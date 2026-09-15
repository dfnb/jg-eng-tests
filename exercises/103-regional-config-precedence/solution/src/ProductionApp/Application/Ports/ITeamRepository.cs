using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Ports;

public interface ITeamRepository
{
    Task<Team?> FindAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<IReadOnlyList<Team>> ListAsync(string tenantId, CancellationToken cancellationToken);
    Task SaveAsync(Team entity, CancellationToken cancellationToken);
    Task<bool> ExistsAsync(string tenantId, string id, CancellationToken cancellationToken);
    Task<int> CountAsync(string tenantId, CancellationToken cancellationToken);
    Task DeleteAsync(string tenantId, string id, CancellationToken cancellationToken);
}
