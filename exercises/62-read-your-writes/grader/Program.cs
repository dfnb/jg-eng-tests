using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("10|10") == "replica");
Check("C02", () => Policy.Evaluate("11|10") == "replica");
Check("C03", () => Policy.Evaluate("9|10") == "primary");
Check("C04", () => Policy.Evaluate("0|0") == "replica");
Check("C05", () => Policy.Evaluate("9000000000|9000000001") == "primary");
