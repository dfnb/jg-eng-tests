using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');return p[0]=="v1"?$"name={p[1]}":$"displayName={p[1]};email={p[2]}";
        }
    }
