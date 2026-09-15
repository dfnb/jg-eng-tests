using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var s=input.Split(',');var add=Array.IndexOf(s,"add-new");var back=Array.IndexOf(s,"backfill");var switchAt=Array.IndexOf(s,"switch-read");var drop=Array.IndexOf(s,"drop-old");return add>=0&&back>add&&switchAt>back&&drop>switchAt?"safe":"unsafe";
        }
    }
