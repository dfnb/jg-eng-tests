namespace ProductionApp.Infrastructure.Configuration;
public sealed record ConfigurationValue(string Key, string Value, string Source, int Priority)
{
    public bool IsUsable => !string.IsNullOrWhiteSpace(Key) && !string.IsNullOrWhiteSpace(Value);
    public static ConfigurationValue Select(IEnumerable<ConfigurationValue> values) =>
        values.Where(x => x.IsUsable).OrderByDescending(x => x.Priority).First();
}
