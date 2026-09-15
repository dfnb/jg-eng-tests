namespace ProductionApp.Api.Contracts;
public sealed record ApiResponse(int Status, string Body, IReadOnlyDictionary<string, string> Headers)
{
    public bool IsSuccess => Status is >= 200 and < 300;
    public static ApiResponse Ok(string body) => new(200, body, new Dictionary<string, string>());
    public static ApiResponse Problem(int status, string code) => new(status, code, new Dictionary<string, string>());
}
