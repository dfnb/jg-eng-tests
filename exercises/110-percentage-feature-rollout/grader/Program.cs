using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","ana|0","off");
Check("C02","ana|100","on");
Check("C03","a|98","on");
Check("C04","a|97","off");
Check("C05","b|99","on");
