using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var active=int.Parse(p[0]);var queued=int.Parse(p[1]);var remaining=int.Parse(p[2]);if(remaining<=0&&active>0)return"force-stop";if(active>0)return$"drain:{active}";return queued>0?"leave-queued":"stopped";
    }
}
