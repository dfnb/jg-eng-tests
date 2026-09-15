using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("closed|failure|3") == "open");
Check("C02", () => Policy.Evaluate("open|timeout|0") == "half-open");
Check("C03", () => Policy.Evaluate("half-open|success|0") == "closed");
Check("C04", () => Policy.Evaluate("half-open|failure|0") == "open");
Check("C05", () => Policy.Evaluate("open|request|0") == "reject");
