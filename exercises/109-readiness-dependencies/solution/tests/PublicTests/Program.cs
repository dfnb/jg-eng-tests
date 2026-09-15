using ProductionApp;
    var value = ScenarioFacade.Execute("required:db:up,required:queue:up");
    if (value != "ready") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
