using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("1|2|wait") == "write");
Check("C02", () => Policy.Evaluate("2|2|wait") == "wait");
Check("C03", () => Policy.Evaluate("2|2|drop-oldest") == "replace-oldest");
Check("C04", () => Policy.Evaluate("2|2|drop-write") == "drop-new");
Check("C05", () => Policy.Evaluate("0|0|wait") == "wait");
