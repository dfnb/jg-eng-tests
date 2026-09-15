namespace ProductionApp.Domain.Entities;

public sealed record Warehouse(
    string Id,
    string TenantId,
    string Status,
    decimal Amount,
    DateTimeOffset CreatedAt,
    DateTimeOffset UpdatedAt)
{
    public bool IsActive => Status is "active" or "open" or "pending";
    public bool BelongsTo(string tenantId) => StringComparer.Ordinal.Equals(TenantId, tenantId);
    public bool HasIdentity(string id) => StringComparer.Ordinal.Equals(Id, id);
    public Warehouse Touch(DateTimeOffset now) => this with { UpdatedAt = now };
    public Warehouse ChangeStatus(string status, DateTimeOffset now) => this with { Status = status.Trim().ToLowerInvariant(), UpdatedAt = now };
    public Warehouse ChangeAmount(decimal amount, DateTimeOffset now) => this with { Amount = amount, UpdatedAt = now };
    public IReadOnlyDictionary<string, string> Tags() => new Dictionary<string, string>
    {
        ["entity"] = "warehouse",
        ["tenant"] = TenantId,
        ["status"] = Status
    };
    public static Warehouse Create(string id, string tenantId, DateTimeOffset now) =>
        new(id.Trim(), tenantId.Trim(), "active", 0m, now, now);
}
