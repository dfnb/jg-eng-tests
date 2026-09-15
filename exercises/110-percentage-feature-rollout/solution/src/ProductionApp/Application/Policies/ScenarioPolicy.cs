using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var percent=int.Parse(p[1]);if(percent<=0)return"off";if(percent>=100)return"on";var bucket=p[0].Aggregate(0,(h,c)=>(h*31+c)%100);return bucket<percent?"on":"off";
    }
}
