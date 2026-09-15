using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","2|a:5:20,b:5:10","b");
Check("C02","5|a:4:1,b:5:9","b");
Check("C03","1|b:2:5,a:2:5","a");
Check("C04","10|a:2:1","unavailable");
Check("C05","1|","unavailable");
