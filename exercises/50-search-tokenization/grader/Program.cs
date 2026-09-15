using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("Red Apple") == "red&apple");
Check("C02", () => Policy.Evaluate(" a   b ") == "a&b");
Check("C03", () => Policy.Evaluate("100%") == "100\\%");
Check("C04", () => Policy.Evaluate("a_b") == "a\\_b");
Check("C05", () => Policy.Evaluate("a\\b") == "a\\\\b");
