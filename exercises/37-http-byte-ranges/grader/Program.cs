using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("100|10|19") == "206|10|10|bytes 10-19/100");
Check("C02", () => Policy.Evaluate("100|99|99") == "206|99|1|bytes 99-99/100");
Check("C03", () => Policy.Evaluate("100|90|100") == "416");
Check("C04", () => Policy.Evaluate("100|20|10") == "416");
Check("C05", () => Policy.Evaluate("100|-1|2") == "416");
