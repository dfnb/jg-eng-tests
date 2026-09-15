using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","tenant=t1,region=br","region=br,tenant=t1");
Check("C02","tenant=t1,token=abc","tenant=t1");
Check("C03","tenant=abcdefghijklmnopqrstuvwxyz","");
Check("C04","tenant=t,request-type=r,region=x","region=x,request-type=r,tenant=t");
Check("C05","","");
