using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("a|100") == "104");
Check("C02", () => Policy.Evaluate("b|100") == "105");
Check("C03", () => Policy.Evaluate("c|20") == "15");
Check("C04", () => Policy.Evaluate("a|10") == "14");
Check("C05", () => Policy.Evaluate("ç|100") == "95");
