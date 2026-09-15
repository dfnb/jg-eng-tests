namespace ProductionApp.Infrastructure.Persistence;
public interface ITransactionBoundary
{
    Task BeginAsync(CancellationToken cancellationToken);
    Task CommitAsync(CancellationToken cancellationToken);
    Task RollbackAsync(CancellationToken cancellationToken);
}
public sealed record TransactionOutcome(bool Committed, string? Error);
