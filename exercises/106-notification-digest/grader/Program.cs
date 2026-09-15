using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","b:email:2,a:sms:1","a:sms:1,b:email:2");
Check("C02","a:email:1,a:email:1","a:email:1");
Check("C03","a:sms:1,a:email:2","a:email:2,a:sms:1");
Check("C04","b:email:1,a:email:1","a:email:1,b:email:1");
Check("C05","","");
