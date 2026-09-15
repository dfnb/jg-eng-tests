using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            return string.Join('&',input.Trim().Split(' ',StringSplitOptions.RemoveEmptyEntries).Select(x=>x.ToLowerInvariant().Replace("\\","\\\\").Replace("%","\\%").Replace("_","\\_")));
        }
    }
