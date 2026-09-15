using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var a=input.ToLowerInvariant();if(a.Contains("text/csv;q=1"))return"csv";if(a.Contains("application/json")&&!a.Contains("application/json;q=0"))return"json";if(a.Contains("text/csv")&&!a.Contains("text/csv;q=0"))return"csv";return"406";
        }
    }
