using Challenge;
    var output = Policy.Evaluate("closed|failure|3");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
