using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}}
C("C01",()=>{var x=new X();return new Checkout(x,x,x).Execute(new("o",1,1))&&x.R==1&&x.P==1&&x.C==1;});
C("C02",()=>{var x=new X{Pay=false};return !new Checkout(x,x,x).Execute(new("o",1,1))&&x.C==0;});
C("C03",()=>{var x=new X{Pay=false};new Checkout(x,x,x).Execute(new("o",1,1));return x.L==1;});
C("C04",()=>{var x=new X();return !new Checkout(x,x,x).Execute(new("o",0,0))&&x.R+x.P+x.C==0;});
C("C05",()=>typeof(Checkout).GetConstructors().Single().GetParameters().All(p=>p.ParameterType.IsInterface));
class X:IStock,IPayment,IOrders{public int R,P,C,L;public bool Pay=true;public bool Reserve(string x){R++;return true;}public void Release(string x)=>L++;public bool Charge(decimal v){P++;return Pay;}public void Confirm(string x)=>C++;}
