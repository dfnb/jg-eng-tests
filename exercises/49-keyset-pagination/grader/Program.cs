using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("9|a|10|z") == "after");
Check("C02", () => Policy.Evaluate("11|a|10|z") == "before");
Check("C03", () => Policy.Evaluate("10|b|10|a") == "after");
Check("C04", () => Policy.Evaluate("10|a|10|a") == "before");
Check("C05", () => Policy.Evaluate("10|B|10|a") == "before");
