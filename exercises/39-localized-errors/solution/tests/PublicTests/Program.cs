using Challenge;
    var output = Policy.Evaluate("pt-BR|errors|1");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
