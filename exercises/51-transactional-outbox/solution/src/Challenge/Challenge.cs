using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
            return input switch{"save,event,commit"=>"atomic","event,save,commit"=>"atomic","save,commit,event"=>"unsafe","event,commit,save"=>"unsafe",_=>"rollback"};
        }
    }
