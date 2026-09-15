using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("404|t1") == "type=not-found;status=404;trace=t1");
Check("C02", () => Policy.Evaluate("409|t2") == "type=conflict;status=409;trace=t2");
Check("C03", () => Policy.Evaluate("422|t3") == "type=validation;status=422;trace=t3");
Check("C04", () => Policy.Evaluate("400|abc") == "type=validation;status=400;trace=abc");
Check("C05", () => Policy.Evaluate("500|z") == "type=validation;status=500;trace=z");
