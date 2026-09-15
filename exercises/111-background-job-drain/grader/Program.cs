using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","2|5|30","drain:2");
Check("C02","1|0|0","force-stop");
Check("C03","0|3|30","leave-queued");
Check("C04","0|0|30","stopped");
Check("C05","1|99|5","drain:1");
