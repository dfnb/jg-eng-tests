using Challenge;
    var output = Policy.Evaluate("v1|Ana|a@x");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
