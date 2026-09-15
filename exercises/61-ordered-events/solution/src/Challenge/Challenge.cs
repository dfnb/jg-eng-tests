using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|').Select(long.Parse).ToArray();return p[1]==p[0]+1?"apply":p[1]<=p[0]?"duplicate":"gap";
        }
    }
