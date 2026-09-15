using Challenge;var q=SearchQuery.Build("apple","name","asc");if(!q.Sql.Contains("SELECT id,name FROM products"))throw new Exception();Console.WriteLine("Public tests passed");
