using ProductionApp;
    var value = ScenarioFacade.Execute("2|5|30");
    if (value != "drain:2") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
