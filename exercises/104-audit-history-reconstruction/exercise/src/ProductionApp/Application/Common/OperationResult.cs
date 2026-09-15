namespace ProductionApp.Application.Common;
public sealed record OperationResult<T>(bool Succeeded, T? Value, string? Error)
{
    public static OperationResult<T> Success(T value) => new(true, value, null);
    public static OperationResult<T> Failure(string error) => new(false, default, error);
    public OperationResult<TResult> Map<TResult>(Func<T, TResult> map) =>
        Succeeded && Value is not null ? OperationResult<TResult>.Success(map(Value)) : OperationResult<TResult>.Failure(Error ?? "unknown");
}
