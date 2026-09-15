using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("v1|Order") == "v3|name=Order|currency=BRL");
Check("C02", () => Policy.Evaluate("v2|Order|USD") == "v3|name=Order|currency=USD");
Check("C03", () => Policy.Evaluate("v3|name=A|currency=EUR") == "v3|name=A|currency=EUR");
Check("C04", () => Policy.Evaluate("v1|Pedido ç") == "v3|name=Pedido ç|currency=BRL");
Check("C05", () => Policy.Evaluate("v1|X") == "v3|name=X|currency=BRL");
