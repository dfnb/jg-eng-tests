using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|').Select(int.Parse).ToArray();var len=p[2]-p[1]+1;return p[1]<0||p[2]<p[1]||p[2]>=p[0]?"416":$"206|{p[1]}|{len}|bytes {p[1]}-{p[2]}/{p[0]}";
        }
    }
