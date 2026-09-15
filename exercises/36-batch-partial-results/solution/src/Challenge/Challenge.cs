using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            return string.Join(',',input.Split(',').Select((x,i)=>x.StartsWith("ok:")?$"{i}:200:{x[3..]}":$"{i}:422:{x[4..]}"));
        }
    }
