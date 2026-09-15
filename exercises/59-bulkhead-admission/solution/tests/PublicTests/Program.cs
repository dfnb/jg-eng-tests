using Challenge;
    var output = Policy.Evaluate("1|0|2|3");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
