using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var needed=int.Parse(p[0]);var candidates=p[1].Split(',',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.Split(':')).Select(x=>(Id:x[0],Stock:int.Parse(x[1]),Distance:int.Parse(x[2]))).Where(x=>x.Stock>=needed).OrderBy(x=>x.Distance).ToArray();return candidates.Length==0?"unavailable":candidates[0].Id;
    }
}
