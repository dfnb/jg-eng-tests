using Challenge;
    var output = Policy.Evaluate("100|10|19");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
