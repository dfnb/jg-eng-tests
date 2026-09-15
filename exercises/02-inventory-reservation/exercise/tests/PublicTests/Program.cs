using Challenge; var d=new Inventory{Available=10}; var s=new ReservationService(d); if(!s.Reserve("r",3)||d.Available!=7)throw new Exception(); Console.WriteLine("Public tests passed");
