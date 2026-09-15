using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","365|365|none|active","delete");
Check("C02","10|365|none|active","keep");
Check("C03","900|365|hold|active","keep");
Check("C04","900|365|none|deleted","skip");
Check("C05","364|365|none|active","keep");
