using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","1|2|2030-01-01","deprecated|sunset=2030-01-01");
Check("C02","2|2|2030-01-01","supported");
Check("C03","3|2|2030-01-01","supported");
Check("C04","1|4|2028-12-31","deprecated|sunset=2028-12-31");
Check("C05","1|1|never","supported");
