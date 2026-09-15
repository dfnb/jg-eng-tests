namespace ProductionApp.Domain.Entities;

public sealed record PriceRule(
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
    public PriceRule Touch(DateTimeOffset now) => this with { UpdatedAt = now };
    public PriceRule ChangeStatus(string status, DateTimeOffset now) => this with { Status = status.Trim().ToLowerInvariant(), UpdatedAt = now };
    public PriceRule ChangeAmount(decimal amount, DateTimeOffset now) => this with { Amount = amount, UpdatedAt = now };
    public IReadOnlyDictionary<string, string> Tags() => new Dictionary<string, string>
    {
        ["entity"] = "pricerule",
        ["tenant"] = TenantId,
        ["status"] = Status
    };
    public static PriceRule Create(string id, string tenantId, DateTimeOffset now) =>
        new(id.Trim(), tenantId.Trim(), "active", 0m, now, now);
}
