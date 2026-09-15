using Challenge;var d=new InboxStore();new Consumer(d).Handle("1");if(d.Invoices.Count!=1)throw new Exception();Console.WriteLine("Public tests passed");
