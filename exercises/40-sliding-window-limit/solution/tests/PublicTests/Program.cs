using Challenge;
    var output = Policy.Evaluate("100|3|50,80");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
