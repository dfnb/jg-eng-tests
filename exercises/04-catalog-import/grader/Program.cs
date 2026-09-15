using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}var q=(char)34;var quoted=$"sku,name,price\nA,{q}Apple, green{q},1.25\nB,{q}Say {q}{q}hi{q}{q}{q},2";
C("C01",()=>CatalogImporter.Parse("sku,name,price\nA,Apple,1.25").Items.Single().Name=="Apple");
C("C02",()=>CatalogImporter.Parse(quoted).Items[1].Name==$"Say {q}hi{q}");
C("C03",()=>CatalogImporter.Parse("sku,name,price\nA,x,1\na,y,2").Errors.Single() is {Line:3,Code:"duplicate_sku"});
C("C04",()=>CatalogImporter.Parse("sku,name,price\nA,x,1\nB,y,no").Items.Count==0);
C("C05",()=>CatalogImporter.Parse("sku,name,price\nA,x,1.25").Items.Single().Price==1.25m);
