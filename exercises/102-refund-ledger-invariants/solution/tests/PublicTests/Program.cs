using ProductionApp;
    var value = ScenarioFacade.Execute("25.5|debit|brl");
    if (value != "credit|25.50|BRL") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
