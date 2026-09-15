using Challenge;
    var output = Policy.Evaluate("100|101|5");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
