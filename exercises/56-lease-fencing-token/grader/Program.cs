using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("11|10") == "accept");
Check("C02", () => Policy.Evaluate("10|10") == "accept");
Check("C03", () => Policy.Evaluate("9|10") == "stale");
Check("C04", () => Policy.Evaluate("0|0") == "accept");
Check("C05", () => Policy.Evaluate("9000000000|8999999999") == "accept");
