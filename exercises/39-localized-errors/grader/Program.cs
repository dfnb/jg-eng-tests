using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("pt-BR|errors|1") == "1 erro");
Check("C02", () => Policy.Evaluate("pt-BR|errors|2") == "2 erros");
Check("C03", () => Policy.Evaluate("en-US|errors|1") == "1 error");
Check("C04", () => Policy.Evaluate("en|errors|0") == "0 errors");
Check("C05", () => Policy.Evaluate("fr|errors|3") == "3 errors");
