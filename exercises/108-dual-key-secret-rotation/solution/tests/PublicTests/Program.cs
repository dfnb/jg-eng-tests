using ProductionApp;
    var value = ScenarioFacade.Execute("k2|k2|k1");
    if (value != "valid") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
