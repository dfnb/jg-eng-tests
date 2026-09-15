using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var allowed=new HashSet<string>{"tenant","request-type","region"};var rows=input.Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split('=',2)).Where(x=>allowed.Contains(x[0])&&x[1].Length<=20).OrderBy(x=>x[0]).Select(x=>$"{x[0]}={x[1]}");return string.Join(',',rows);
    }
}
