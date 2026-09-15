using Challenge;
    var output = Policy.Evaluate("product-1|detail:product-1,list:catalog+product-1,other:user-1");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
