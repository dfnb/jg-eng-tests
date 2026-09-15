using Challenge;
    var output = Policy.Evaluate("k|new|h1");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
