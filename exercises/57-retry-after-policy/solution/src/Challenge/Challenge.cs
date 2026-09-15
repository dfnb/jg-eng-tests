using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');if(!int.TryParse(p[0],out var seconds)||seconds<0)return"invalid";return Math.Min(seconds,int.Parse(p[1])).ToString();
        }
    }
