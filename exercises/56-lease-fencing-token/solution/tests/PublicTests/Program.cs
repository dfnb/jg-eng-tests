using Challenge;
    var output = Policy.Evaluate("11|10");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
