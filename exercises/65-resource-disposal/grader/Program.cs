using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("db,file") == "dispose-file,dispose-db");
Check("C02", () => Policy.Evaluate("db,fail:file") == "dispose-db");
Check("C03", () => Policy.Evaluate("fail:db") == "");
Check("C04", () => Policy.Evaluate("a,b,c") == "dispose-c,dispose-b,dispose-a");
Check("C05", () => Policy.Evaluate("") == "");
