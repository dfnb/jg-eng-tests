using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("old|~") == "old");
Check("C02", () => Policy.Evaluate("old|null") == "<cleared>");
Check("C03", () => Policy.Evaluate("old|new") == "new");
Check("C04", () => Policy.Evaluate("old| new ") == "new");
Check("C05", () => Policy.Evaluate("old|") == "");
