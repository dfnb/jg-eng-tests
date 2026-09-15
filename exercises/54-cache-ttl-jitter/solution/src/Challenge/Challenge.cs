using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var baseTtl=int.Parse(p[1]);var jitter=p[0].Sum(c=>(int)c)%11-5;return (baseTtl+jitter).ToString();
        }
    }
