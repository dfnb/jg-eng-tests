using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var at=long.Parse(p[0]);var values=p[1].Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split(':')).Where(x=>long.Parse(x[0])<=at).ToArray();return values.Length==0?"missing":values[^1][1];
    }
}
