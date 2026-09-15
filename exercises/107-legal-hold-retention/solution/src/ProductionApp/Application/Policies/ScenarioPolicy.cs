using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var age=int.Parse(p[0]);var retention=int.Parse(p[1]);if(p[2]=="hold")return"keep";if(p[3]=="deleted")return"skip";return age>=retention?"delete":"keep";
    }
}
