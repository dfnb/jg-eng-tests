using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("v1|Ana|a@x") == "name=Ana");
Check("C02", () => Policy.Evaluate("v2|Ana|a@x") == "displayName=Ana;email=a@x");
Check("C03", () => Policy.Evaluate("v1||a@x") == "name=");
Check("C04", () => Policy.Evaluate("v2|João|j@x") == "displayName=João;email=j@x");
Check("C05", () => Policy.Evaluate("v3|A|b@x") == "displayName=A;email=b@x");
