using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var at=long.Parse(p[0]);var events=p[1].Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split(':')).Select(x=>(At:long.Parse(x[0]),Value:x[1])).Where(x=>x.At<=at).OrderBy(x=>x.At).ToArray();return events.Length==0?"missing":events[^1].Value;
    }
}
