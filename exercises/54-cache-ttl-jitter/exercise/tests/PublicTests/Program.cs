using Challenge;
    var output = Policy.Evaluate("a|100");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
