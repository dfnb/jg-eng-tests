using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');return new[]{p[2],p[1],p[0]}.FirstOrDefault(x=>!string.IsNullOrWhiteSpace(x))??"unset";
    }
}
