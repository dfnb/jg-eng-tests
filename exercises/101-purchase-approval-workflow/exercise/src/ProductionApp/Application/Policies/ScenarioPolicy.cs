using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var amount=decimal.Parse(p[0],CultureInfo.InvariantCulture);return amount>=1000m?"manager-approval":"approved";
    }
}
