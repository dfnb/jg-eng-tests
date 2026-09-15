using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var type=p[0] switch{"404"=>"not-found","409"=>"conflict",_=>"validation"};return $"type={type};status={p[0]};trace={p[1]}";
        }
    }
