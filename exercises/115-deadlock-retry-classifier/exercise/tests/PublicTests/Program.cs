using ProductionApp;
    var value = ScenarioFacade.Execute("deadlock|1|3");
    if (value != "retry") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
