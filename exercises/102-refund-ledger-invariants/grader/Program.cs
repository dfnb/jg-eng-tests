using ProductionApp;
void Check(string id,string input,string expected){try{Console.WriteLine($"{id}|{(ScenarioFacade.Execute(input)==expected?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
Check("C01","25.5|debit|brl","credit|25.50|BRL");
Check("C02","10|credit|USD","debit|10.00|USD");
Check("C03","0.01|debit|EUR","credit|0.01|EUR");
Check("C04","99.99|credit|brl","debit|99.99|BRL");
Check("C05","1|debit|gbp","credit|1.00|GBP");
