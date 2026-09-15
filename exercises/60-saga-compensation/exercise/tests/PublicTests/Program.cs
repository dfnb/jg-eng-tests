using Challenge;
    var output = Policy.Evaluate("stock,payment,fail:shipping");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
