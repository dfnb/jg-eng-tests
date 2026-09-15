using Challenge;var r=new CatalogRepository([new("a","A")],new(){{"a",2}});if(new CatalogService(r).List(0,1).Single().Stock!=2)throw new Exception();Console.WriteLine("Public tests passed");
