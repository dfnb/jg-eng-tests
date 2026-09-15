using Challenge;var d=new Dictionary<string,Order>{{"1",new("1","a","New","")}};if(new Orders(d).Get("a","1") is null)throw new Exception();Console.WriteLine("Public tests passed");
