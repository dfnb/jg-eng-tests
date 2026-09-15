using Challenge;
    var output = Policy.Evaluate("add-new,backfill,switch-read,drop-old");
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
