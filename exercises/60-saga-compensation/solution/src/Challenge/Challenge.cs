using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var done=input.Split(',',StringSplitOptions.RemoveEmptyEntries).TakeWhile(x=>!x.StartsWith("fail:")).ToArray();return string.Join(',',done.Reverse().Select(x=>"undo-"+x));
        }
    }
