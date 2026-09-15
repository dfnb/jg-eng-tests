namespace ProductionApp.Application.Common;
public sealed record PageSlice<T>(IReadOnlyList<T> Items, string? NextCursor, int Total)
{
    public bool HasMore => NextCursor is not null;
    public static PageSlice<T> Empty() => new(Array.Empty<T>(), null, 0);
    public PageSlice<TResult> Map<TResult>(Func<T, TResult> map) => new(Items.Select(map).ToArray(), NextCursor, Total);
}
