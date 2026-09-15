using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ProductionApp.Application.Policies;

internal static class ScenarioPolicy
{
    internal static string Evaluate(string input)
    {
        var p=input.Split('|');var presented=p[0];var current=p[1];var previous=p[2];return CryptographicOperations.FixedTimeEquals(Encoding.UTF8.GetBytes(presented),Encoding.UTF8.GetBytes(current))||(!string.IsNullOrEmpty(previous)&&CryptographicOperations.FixedTimeEquals(Encoding.UTF8.GetBytes(presented),Encoding.UTF8.GetBytes(previous)))?"valid":"invalid";
    }
}
