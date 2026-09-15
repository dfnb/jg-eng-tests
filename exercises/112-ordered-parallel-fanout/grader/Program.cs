using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","slow,fast","0:ok:slow,1:ok:fast");
Check("C02","a,fail:b,c","0:ok:a,1:error:b,2:ok:c");
Check("C03","fail:a,fail:b","0:error:a,1:error:b");
Check("C04","x","0:ok:x");
Check("C05","","");
