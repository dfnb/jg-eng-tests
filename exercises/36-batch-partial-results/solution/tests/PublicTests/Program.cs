using Challenge;
    var output = Policy.Evaluate("ok:a,err:b");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
