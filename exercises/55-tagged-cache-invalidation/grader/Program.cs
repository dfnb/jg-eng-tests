using Challenge;
static void Check(string id, Func<bool> test)
{
    try { Console.WriteLine($"{id}|{(test() ? "pass" : "fail")}"); }
    catch (Exception error) { Console.WriteLine($"{id}|fail|{error.GetType().Name}"); }
}
Check("C01", () => Policy.Evaluate("product-1|detail:product-1,list:catalog+product-1,other:user-1") == "detail,list");
Check("C02", () => Policy.Evaluate("user-1|catalog:product-1,profile:user-1") == "profile");
Check("C03", () => Policy.Evaluate("x|a:y,b:z") == "");
Check("C04", () => Policy.Evaluate("b|x:a+b,y:b+c") == "x,y");
Check("C05", () => Policy.Evaluate("t|z:t,a:t") == "a,z");
