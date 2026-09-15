using ProductionApp;
    var value = ScenarioFacade.Execute("20|10:draft,20:open,30:closed");
    if (value != "open") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
