using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');return p[1] switch{"~"=>p[0],"null"=>"<cleared>",_=>p[1].Trim()};
        }
    }
