using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var s=int.Parse(p[0]);var cs=int.Parse(p[2]);return s<cs||s==cs&&string.CompareOrdinal(p[1],p[3])>0?"after":"before";
        }
    }
