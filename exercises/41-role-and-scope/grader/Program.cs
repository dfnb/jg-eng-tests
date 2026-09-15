using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("admin|orders:write") == "allow");
Check("C02", () => Policy.Evaluate("admin|orders:read") == "deny");
Check("C03", () => Policy.Evaluate("user|orders:write") == "deny");
Check("C04", () => Policy.Evaluate("user,admin|profile,orders:write") == "allow");
Check("C05", () => Policy.Evaluate("superadmin|orders:writer") == "deny");
