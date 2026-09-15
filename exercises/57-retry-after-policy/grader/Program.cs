using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("5|30") == "5");
Check("C02", () => Policy.Evaluate("120|30") == "30");
Check("C03", () => Policy.Evaluate("0|30") == "0");
Check("C04", () => Policy.Evaluate("-1|30") == "invalid");
Check("C05", () => Policy.Evaluate("tomorrow|30") == "invalid");
