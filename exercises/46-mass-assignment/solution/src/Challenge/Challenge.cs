using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var allowed=new HashSet<string>{"name","phone"};return string.Join(',',input.Split(',').Where(x=>allowed.Contains(x.Split('=')[0])).OrderBy(x=>x));
        }
    }
