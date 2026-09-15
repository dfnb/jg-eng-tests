using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var version=int.Parse(p[0]);var current=int.Parse(p[1]);var sunset=p[2];return version<current?$"deprecated|sunset={sunset}":"supported";
    }
}
