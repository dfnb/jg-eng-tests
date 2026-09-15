using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("https://example.com/a") == "allow");
Check("C02", () => Policy.Evaluate("http://example.com") == "deny");
Check("C03", () => Policy.Evaluate("https://localhost/x") == "deny");
Check("C04", () => Policy.Evaluate("https://169.254.1.1/x") == "deny");
Check("C05", () => Policy.Evaluate("https://u:p@example.com") == "deny");
