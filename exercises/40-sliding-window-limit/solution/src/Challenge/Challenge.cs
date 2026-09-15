using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var now=int.Parse(p[0]);var limit=int.Parse(p[1]);var count=p[2].Split(',',StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).Count(x=>x>now-60);return count<limit?"allow":"deny";
        }
    }
