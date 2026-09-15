using Challenge;
    var output = Policy.Evaluate("admin|orders:write");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
