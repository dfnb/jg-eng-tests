using ProductionApp;
    var value = ScenarioFacade.Execute("2|a:5:20,b:5:10");
    if (value != "b") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
