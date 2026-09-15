using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("10|12") == "rehash");
Check("C02", () => Policy.Evaluate("12|12") == "keep");
Check("C03", () => Policy.Evaluate("14|12") == "keep");
Check("C04", () => Policy.Evaluate("0|1") == "rehash");
Check("C05", () => Policy.Evaluate("12|10") == "keep");
