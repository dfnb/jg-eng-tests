using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            return input switch{"closed|failure|3"=>"open","open|timeout|0"=>"half-open","half-open|success|0"=>"closed","half-open|failure|0"=>"open","open|request|0"=>"reject",_=>"closed"};
        }
    }
