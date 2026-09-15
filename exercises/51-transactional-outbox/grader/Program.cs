using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("save,event,commit") == "atomic");
Check("C02", () => Policy.Evaluate("event,save,commit") == "atomic");
Check("C03", () => Policy.Evaluate("save,commit,event") == "unsafe");
Check("C04", () => Policy.Evaluate("event,commit,save") == "unsafe");
Check("C05", () => Policy.Evaluate("save,event,fail") == "rollback");
