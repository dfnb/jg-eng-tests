using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("7|7") == "updated");
Check("C02", () => Policy.Evaluate("7|6") == "precondition-failed");
Check("C03", () => Policy.Evaluate("7|8") == "precondition-failed");
Check("C04", () => Policy.Evaluate("7|") == "precondition-failed");
Check("C05", () => Policy.Evaluate("v2|v2") == "updated");
