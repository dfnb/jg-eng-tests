using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","k2|k2|k1","valid");
Check("C02","k1|k2|k1","valid");
Check("C03","k0|k2|k1","invalid");
Check("C04","|k2|","invalid");
Check("C05","K2|k2|k1","invalid");
