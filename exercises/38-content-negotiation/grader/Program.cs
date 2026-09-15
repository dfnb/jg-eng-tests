using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("application/json") == "json");
Check("C02", () => Policy.Evaluate("text/csv") == "csv");
Check("C03", () => Policy.Evaluate("application/json;q=0.5,text/csv;q=1") == "csv");
Check("C04", () => Policy.Evaluate("application/json;q=0,text/csv;q=0") == "406");
Check("C05", () => Policy.Evaluate("image/png") == "406");
