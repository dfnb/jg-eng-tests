using Challenge;var t=DateTimeOffset.UtcNow;if(Paginator.Page([new("a",t)],null,null,10).Single().Id!="a")throw new Exception();Console.WriteLine("Public tests passed");
