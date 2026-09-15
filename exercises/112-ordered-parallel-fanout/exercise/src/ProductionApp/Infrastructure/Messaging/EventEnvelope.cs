namespace ProductionApp.Infrastructure.Messaging;
public sealed record EventEnvelope(string Id, string Type, int Version, string TenantId, DateTimeOffset OccurredAt, string Payload)
{
    public bool IsCurrent(int version) => Version == version;
    public EventEnvelope Upgrade(int version, string payload) => this with { Version = version, Payload = payload };
    public string PartitionKey() => $"{TenantId}:{Type}";
}
