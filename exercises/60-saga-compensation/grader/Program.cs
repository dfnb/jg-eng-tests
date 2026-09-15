using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("stock,payment,fail:shipping") == "undo-payment,undo-stock");
Check("C02", () => Policy.Evaluate("fail:stock") == "");
Check("C03", () => Policy.Evaluate("stock,payment") == "undo-payment,undo-stock");
Check("C04", () => Policy.Evaluate("stock,fail:payment") == "undo-stock");
Check("C05", () => Policy.Evaluate("") == "");
