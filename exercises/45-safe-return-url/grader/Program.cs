using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("/orders/1") == "/orders/1");
Check("C02", () => Policy.Evaluate("https://evil.test") == "/");
Check("C03", () => Policy.Evaluate("//evil.test/x") == "/");
Check("C04", () => Policy.Evaluate("orders") == "/");
Check("C05", () => Policy.Evaluate("/search?q=x") == "/search?q=x");
