using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var rows=input.Split(',',StringSplitOptions.RemoveEmptyEntries).Select((x,i)=>x.StartsWith("fail:")?$"{i}:error:{x[5..]}":$"{i}:ok:{x}");return string.Join(',',rows);
    }
}
