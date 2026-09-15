using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("user=a;password=secret") == "user=a;password=<redacted>");
Check("C02", () => Policy.Evaluate("token=abc;trace=1") == "token=<redacted>;trace=1");
Check("C03", () => Policy.Evaluate("Authorization=Bearer x") == "Authorization=<redacted>");
Check("C04", () => Policy.Evaluate("email=a@x") == "email=a@x");
Check("C05", () => Policy.Evaluate("password=x;token=y") == "password=<redacted>;token=<redacted>");
