using Challenge;
    var output = Policy.Evaluate("name=Ana");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
