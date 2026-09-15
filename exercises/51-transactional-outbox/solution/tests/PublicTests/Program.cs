using Challenge;
    var output = Policy.Evaluate("save,event,commit");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
