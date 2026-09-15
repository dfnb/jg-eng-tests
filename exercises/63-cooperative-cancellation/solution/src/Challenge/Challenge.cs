using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|').Select(int.Parse).ToArray();if(p[2]<0)return p[0].ToString();var boundary=((p[2]/p[1])+1)*p[1];return Math.Min(p[0],boundary).ToString();
        }
    }
