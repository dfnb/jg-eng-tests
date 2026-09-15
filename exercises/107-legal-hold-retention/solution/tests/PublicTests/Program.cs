using ProductionApp;
    var value = ScenarioFacade.Execute("365|365|none|active");
    if (value != "delete") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
