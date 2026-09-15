using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var n=int.Parse(p[2]);var lang=p[0].StartsWith("pt")?"pt":"en";return lang=="pt"?(n==1?$"{n} erro":$"{n} erros"):(n==1?$"{n} error":$"{n} errors");
        }
    }
