namespace ProductionApp.Infrastructure.Health;
public sealed record DependencySnapshot(string Name, bool Required, bool Available, TimeSpan Latency)
{
    public string State => Available ? "up" : "down";
    public bool BlocksReadiness => Required && !Available;
    public static DependencySnapshot Up(string name, bool required) => new(name, required, true, TimeSpan.Zero);
    public static DependencySnapshot Down(string name, bool required) => new(name, required, false, TimeSpan.Zero);
}
