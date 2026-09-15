using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("k|new|h1") == "created");
Check("C02", () => Policy.Evaluate("k|h1|h1") == "replayed");
Check("C03", () => Policy.Evaluate("k|h1|h2") == "conflict");
Check("C04", () => Policy.Evaluate("k|empty|empty") == "replayed");
Check("C05", () => Policy.Evaluate("k|H|h") == "conflict");
