using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("Alice") == "ALICE");
Check("C02", () => Policy.Evaluate("ＡＢＣ") == "ABC");
Check("C03", () => Policy.Evaluate("joão") == "JOÃO");
Check("C04", () => Policy.Evaluate("①") == "1");
Check("C05", () => Policy.Evaluate(" A ") == " A ");
