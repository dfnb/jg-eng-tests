using Challenge;
if(Pricing.Total("Bronze",[new(10m,2)],.1m)!=22m) throw new Exception("baseline");
Console.WriteLine("Public tests passed");
