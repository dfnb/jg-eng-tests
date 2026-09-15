using ProductionApp;
    var value = ScenarioFacade.Execute("slow,fast");
    if (value != "0:ok:slow,1:ok:fast") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
