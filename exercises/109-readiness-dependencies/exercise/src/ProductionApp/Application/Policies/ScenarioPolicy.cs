using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var states=input.Split(',',StringSplitOptions.RemoveEmptyEntries);return states.All(x=>x.EndsWith(":up"))?"ready":"not-ready";
    }
}
