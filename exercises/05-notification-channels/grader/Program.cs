using Challenge;void C(string id,Func<bool> f){try{Console.WriteLine($"{id}|{(f()?"pass":"fail")}");}catch{Console.WriteLine($"{id}|fail");}};
C("C01",()=>{var a=new F("sms");var b=new F("push");new Notifier([a,b]).Send("u","m",["sms","push"]);return a.N==1&&b.N==1;});
C("C02",()=>new Notifier([]).Send("u","m",["fax"]).Count==0);
C("C03",()=>{var a=new F("bad",true);var b=new F("ok");var r=new Notifier([a,b]).Send("u","m",["bad","ok"]);return b.N==1&&r.Count==2;});
C("C04",()=>{var a=new F("carrier-pigeon");new Notifier([a]).Send("u","m",["carrier-pigeon"]);return a.N==1;});
C("C05",()=>{var a=new F("bad",true);var r=new Notifier([a]).Send("u","m",["bad"]);return !r.Single().Success;});
class F(string name,bool fail=false):IChannel{public string Name=>name;public int N;public void Send(string u,string m){N++;if(fail)throw new Exception();}}
