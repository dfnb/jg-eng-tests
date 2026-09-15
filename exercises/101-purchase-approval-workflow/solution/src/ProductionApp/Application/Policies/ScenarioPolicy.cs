using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var amount=decimal.Parse(p[0],CultureInfo.InvariantCulture);var requester=p[1];var approver=p[2];var budget=p[3]=="yes";if(!budget)return"budget-rejected";if(requester==approver)return"segregation-required";return amount>=10000m?"director-approval":amount>=1000m?"manager-approval":"approved";
    }
}
