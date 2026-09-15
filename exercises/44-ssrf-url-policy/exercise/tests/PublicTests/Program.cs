using Challenge;
    var output = Policy.Evaluate("https://example.com/a");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
