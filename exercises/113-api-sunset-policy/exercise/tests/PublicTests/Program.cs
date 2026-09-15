using ProductionApp;
    var value = ScenarioFacade.Execute("1|2|2030-01-01");
    if (value != "deprecated|sunset=2030-01-01") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
