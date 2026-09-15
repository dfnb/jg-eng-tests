using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","500|ana|bia|yes","approved");
Check("C02","1000|ana|bia|yes","manager-approval");
Check("C03","10000|ana|bia|yes","director-approval");
Check("C04","100|ana|bia|no","budget-rejected");
Check("C05","100|ana|ana|yes","segregation-required");
