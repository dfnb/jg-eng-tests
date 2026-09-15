using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","20|10:draft,20:open,30:closed","open");
Check("C02","25|20:open,30:closed,10:draft","open");
Check("C03","5|10:draft","missing");
Check("C04","10|10:draft","draft");
Check("C05","10|","missing");
