using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","global|regional|tenant","tenant");
Check("C02","global|regional|","regional");
Check("C03","global||","global");
Check("C04","global|regional|   ","regional");
Check("C05","||","unset");
