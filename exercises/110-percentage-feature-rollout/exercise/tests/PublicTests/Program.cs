using ProductionApp;
    var value = ScenarioFacade.Execute("ana|0");
    if (value != "off") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
