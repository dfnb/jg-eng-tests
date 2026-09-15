using Challenge;
    var output = Policy.Evaluate("5|30");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
