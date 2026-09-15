using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');return p[0] switch{"v1"=>$"v3|name={p[1]}|currency=BRL","v2"=>$"v3|name={p[1]}|currency={p[2]}",_=>input};
        }
    }
