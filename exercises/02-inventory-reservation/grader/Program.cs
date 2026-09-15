using Challenge;
void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}
C("C01",()=>{var d=new Inventory{Available=10};var s=new ReservationService(d);s.Reserve("r",3);return s.Cancel("r")&&d.Available==10;});
C("C02",()=>{var d=new Inventory{Available=10};var s=new ReservationService(d);s.Reserve("r",3);s.Cancel("r");return !s.Cancel("r")&&d.Available==10;});
C("C03",()=>{var d=new Inventory{Available=5};return new ReservationService(d).Reserve("x",5)&&d.Available==0;});
C("C04",()=>{var d=new Inventory{Available=1};return !new ReservationService(d).Reserve("x",2)&&d.Reservations.Count==0;});
C("C05",()=>{var d=new Inventory{Available=10};var s=new ReservationService(d);s.Reserve("r",3);Parallel.For(0,20,_=>s.Cancel("r"));return d.Available==10;});
