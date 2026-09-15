using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            var p=input.Split('|');var count=int.Parse(p[0]);var cap=int.Parse(p[1]);if(count<cap)return"write";return p[2] switch{"wait"=>"wait","drop-oldest"=>"replace-oldest",_=>"drop-new"};
        }
    }
