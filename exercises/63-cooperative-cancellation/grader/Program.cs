using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("100|10|3") == "10");
Check("C02", () => Policy.Evaluate("100|10|10") == "20");
Check("C03", () => Policy.Evaluate("25|10|-1") == "25");
Check("C04", () => Policy.Evaluate("5|10|2") == "5");
Check("C05", () => Policy.Evaluate("8|1|3") == "4");
