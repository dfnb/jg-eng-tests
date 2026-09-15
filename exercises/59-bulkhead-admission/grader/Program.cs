using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("1|0|2|3") == "run");
Check("C02", () => Policy.Evaluate("2|1|2|3") == "queue");
Check("C03", () => Policy.Evaluate("2|3|2|3") == "reject");
Check("C04", () => Policy.Evaluate("0|0|0|1") == "queue");
Check("C05", () => Policy.Evaluate("0|0|0|0") == "reject");
