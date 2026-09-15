using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            return Regex.Replace(input,"(?i)(password|token|authorization)=([^;]*)","$1=<redacted>");
        }
    }
