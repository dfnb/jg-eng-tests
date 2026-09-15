using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split(',',StringSplitOptions.RemoveEmptyEntries);var acquired=p.TakeWhile(x=>!x.StartsWith("fail:")).ToArray();return string.Join(',',acquired.Reverse().Select(x=>"dispose-"+x));
        }
    }
