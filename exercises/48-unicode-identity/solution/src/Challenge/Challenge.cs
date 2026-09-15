using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            return input.Normalize(NormalizationForm.FormKC).ToUpperInvariant();
        }
    }
