using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("100|101|5") == "valid");
Check("C02", () => Policy.Evaluate("100|100|0") == "valid");
Check("C03", () => Policy.Evaluate("105|100|5") == "valid");
Check("C04", () => Policy.Evaluate("106|100|5") == "expired");
Check("C05", () => Policy.Evaluate("101|100|0") == "expired");
