using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var rows=input.Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split(':')).Select(x=>$"{x[0]}:{x[1]}:{x[2]}").Distinct().OrderBy(x=>x.Split(':')[0]).ThenBy(x=>x.Split(':')[1]);return string.Join(',',rows);
    }
}
