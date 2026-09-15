using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","required:db:up,required:queue:up","ready");
Check("C02","required:db:down,required:queue:up","not-ready");
Check("C03","required:db:up,optional:analytics:down","ready");
Check("C04","optional:x:down","ready");
Check("C05","","ready");
