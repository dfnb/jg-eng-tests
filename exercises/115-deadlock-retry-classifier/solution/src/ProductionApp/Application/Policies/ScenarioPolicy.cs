using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var code=p[0];var attempt=int.Parse(p[1]);var max=int.Parse(p[2]);return code=="deadlock"&&attempt<max?"retry":code=="deadlock"?"exhausted":"fail";
    }
}
