using ProductionApp;
    var value = ScenarioFacade.Execute("b:email:2,a:sms:1");
    if (value != "a:sms:1,b:email:2") throw new Exception($"Resultado básico inesperado: {value}");
    Console.WriteLine("public-tests: ok");
