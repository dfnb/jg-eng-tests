namespace ProductionApp.Application.Common;
public interface IApplicationClock { DateTimeOffset UtcNow { get; } }
public sealed class SystemApplicationClock : IApplicationClock { public DateTimeOffset UtcNow => DateTimeOffset.UtcNow; }
public sealed class FixedApplicationClock(DateTimeOffset value) : IApplicationClock { public DateTimeOffset UtcNow { get; set; } = value; }
