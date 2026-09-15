using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}var t=new DateTimeOffset(2025,1,1,0,0,0,TimeSpan.Zero);
C("C01",()=>Reports.Sales([new("p",10,1,t,"Cancelled"),new("p",5,2,t,"Completed")],t,t.AddDays(1),0,10).Single() is {Revenue:5,Quantity:2});
C("C02",()=>Reports.Sales([new("a",1,1,t,"Completed"),new("b",1,1,t.AddDays(1),"Completed")],t,t.AddDays(1),0,10).Count==1);
C("C03",()=>Reports.Sales([new("a",3,1,t,"Completed"),new("a",4,1,t,"Completed"),new("b",6,1,t,"Completed")],t,t.AddDays(1),0,1).Single().ProductId=="a");
C("C04",()=>string.Join(',',Reports.Sales([new("b",1,1,t,"Completed"),new("a",1,1,t,"Completed")],t,t.AddDays(1),0,2).Select(x=>x.ProductId))=="a,b");
C("C05",()=>{try{Reports.Sales([],t,t,0,0);return false;}catch(ArgumentOutOfRangeException){return true;}});
