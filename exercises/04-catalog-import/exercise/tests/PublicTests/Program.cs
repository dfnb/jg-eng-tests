using Challenge;var r=CatalogImporter.Parse("sku,name,price\nA,Apple,1.50");if(r.Items.Single().Price!=1.5m)throw new Exception();Console.WriteLine("Public tests passed");
