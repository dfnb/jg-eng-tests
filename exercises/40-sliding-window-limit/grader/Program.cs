using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("100|3|50,80") == "allow");
Check("C02", () => Policy.Evaluate("100|2|80,90") == "deny");
Check("C03", () => Policy.Evaluate("100|1|40") == "allow");
Check("C04", () => Policy.Evaluate("100|0|") == "deny");
Check("C05", () => Policy.Evaluate("100|1|40") == "allow");
