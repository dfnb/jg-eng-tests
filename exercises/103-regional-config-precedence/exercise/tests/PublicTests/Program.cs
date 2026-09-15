using ProductionApp;
    var value = ScenarioFacade.Execute("global|regional|tenant");
    if (value != "tenant") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
