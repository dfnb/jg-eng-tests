using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        return string.Join(',',input.Split(',',StringSplitOptions.RemoveEmptyEntries).OrderBy(x=>x.Split(':')[0]));
    }
}
