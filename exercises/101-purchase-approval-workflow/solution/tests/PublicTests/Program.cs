using ProductionApp;
    var value = ScenarioFacade.Execute("500|ana|bia|yes");
    if (value != "approved") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
