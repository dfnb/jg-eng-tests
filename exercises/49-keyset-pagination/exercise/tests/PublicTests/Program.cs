using Challenge;
    var output = Policy.Evaluate("9|a|10|z");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
