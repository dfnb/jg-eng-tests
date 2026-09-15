using Challenge;
void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch(Exception e){Console.WriteLine($"{id}|fail|{e.GetType().Name}");}}
C("C01",()=>Pricing.Total("Gold",[new(100m,1)],0m)==90m);
C("C02",()=>Pricing.Total("silver",[new(100m,1)],0m)==95m);
C("C03",()=>Pricing.Total("Gold",[new(100m,1)],.10m)==99m);
C("C04",()=>Pricing.Total("Platinum",[new(10m,1)],0m)==10m);
C("C05",()=>Pricing.Total("Gold",[new(.05m,1)],0m)==.05m);
