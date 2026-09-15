using ProductionApp;
    var value = ScenarioFacade.Execute("tenant=t1,region=br");
    if (value != "region=br,tenant=t1") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
