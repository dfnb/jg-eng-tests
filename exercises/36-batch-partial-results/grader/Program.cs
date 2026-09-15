using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("ok:a,err:b") == "0:200:a,1:422:b");
Check("C02", () => Policy.Evaluate("ok:a,ok:b") == "0:200:a,1:200:b");
Check("C03", () => Policy.Evaluate("err:a,err:b") == "0:422:a,1:422:b");
Check("C04", () => Policy.Evaluate("ok:z") == "0:200:z");
Check("C05", () => Policy.Evaluate("err:x,ok:y,err:z") == "0:422:x,1:200:y,2:422:z");
