using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var tag=p[0];return string.Join(',',p[1].Split(',').Where(x=>x.Split(':')[1].Split('+').Contains(tag)).Select(x=>x.Split(':')[0]).OrderBy(x=>x));
        }
    }
