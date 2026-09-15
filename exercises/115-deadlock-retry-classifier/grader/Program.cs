using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","deadlock|1|3","retry");
Check("C02","deadlock|3|3","exhausted");
Check("C03","unique|1|3","fail");
Check("C04","timeout|1|3","fail");
Check("C05","deadlock|0|1","retry");
