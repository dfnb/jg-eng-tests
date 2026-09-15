using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            if(!Uri.TryCreate(input,UriKind.Absolute,out var u)||u.Scheme!="https"||!string.IsNullOrEmpty(u.UserInfo))return"deny";var h=u.Host.ToLowerInvariant();return h=="localhost"||h.StartsWith("127.")||h.StartsWith("169.254.")||h=="::1"?"deny":"allow";
        }
    }
