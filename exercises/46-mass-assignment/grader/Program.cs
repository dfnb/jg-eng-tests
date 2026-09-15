using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("name=Ana") == "name=Ana");
Check("C02", () => Policy.Evaluate("name=Ana,role=admin") == "name=Ana");
Check("C03", () => Policy.Evaluate("owner=bob,phone=1") == "phone=1");
Check("C04", () => Policy.Evaluate("phone=2,name=B") == "name=B,phone=2");
Check("C05", () => Policy.Evaluate("role=admin,active=true") == "");
