using ProductionApp.Application.Common;
using ProductionApp.Application.Ports;
using ProductionApp.Domain.Entities;

namespace ProductionApp.Application.Services;

public sealed class PaymentService(IPaymentRepository repository, IApplicationClock clock)
{
    public Task<Payment?> FindAsync(string tenantId, string id, CancellationToken cancellationToken) =>
        repository.FindAsync(tenantId, id, cancellationToken);

    public async Task<OperationResult<Payment>> SaveAsync(Payment entity, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(entity.Id)) return OperationResult<Payment>.Failure("id-required");
        if (string.IsNullOrWhiteSpace(entity.TenantId)) return OperationResult<Payment>.Failure("tenant-required");
        var normalized = entity.Touch(clock.UtcNow);
        await repository.SaveAsync(normalized, cancellationToken);
        return OperationResult<Payment>.Success(normalized);
    }

    public async Task<IReadOnlyList<Payment>> ActiveAsync(string tenantId, CancellationToken cancellationToken)
    {
        var rows = await repository.ListAsync(tenantId, cancellationToken);
        return rows.Where(row => row.IsActive).OrderBy(row => row.Id, StringComparer.Ordinal).ToArray();
    }
}
