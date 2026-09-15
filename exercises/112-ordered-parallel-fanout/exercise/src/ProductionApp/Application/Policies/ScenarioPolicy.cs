using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        if(input.Split(',').Any(x=>x.StartsWith("fail:")))return"batch-error";return string.Join(',',input.Split(',',StringSplitOptions.RemoveEmptyEntries).Select((x,i)=>$"{i}:ok:{x}"));
    }
}
