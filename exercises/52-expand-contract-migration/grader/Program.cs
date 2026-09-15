using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("add-new,backfill,switch-read,drop-old") == "safe");
Check("C02", () => Policy.Evaluate("drop-old,add-new,backfill,switch-read") == "unsafe");
Check("C03", () => Policy.Evaluate("backfill,add-new,switch-read,drop-old") == "unsafe");
Check("C04", () => Policy.Evaluate("add-new,switch-read,backfill,drop-old") == "unsafe");
Check("C05", () => Policy.Evaluate("add-new,backfill,switch-read") == "unsafe");
