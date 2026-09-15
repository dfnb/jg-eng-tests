using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("4|5") == "apply");
Check("C02", () => Policy.Evaluate("5|5") == "duplicate");
Check("C03", () => Policy.Evaluate("5|3") == "duplicate");
Check("C04", () => Policy.Evaluate("5|7") == "gap");
Check("C05", () => Policy.Evaluate("0|1") == "apply");
