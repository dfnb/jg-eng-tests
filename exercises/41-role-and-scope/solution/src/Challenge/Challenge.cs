using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');return p[0].Split(',').Contains("admin")&&p[1].Split(',').Contains("orders:write")?"allow":"deny";
        }
    }
