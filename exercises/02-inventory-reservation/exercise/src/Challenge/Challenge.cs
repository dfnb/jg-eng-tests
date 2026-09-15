namespace Challenge;
public sealed class Inventory { public int Available; public Dictionary<string,(int Qty,string State)> Reservations=new(); }
public sealed class ReservationService(Inventory data) {
 public bool Reserve(string id,int qty){ if(qty<=0||data.Available<qty)return false; data.Available-=qty; data.Reservations[id]=(qty,"Active"); return true; }
 public bool Cancel(string id){ if(!data.Reservations.TryGetValue(id,out var r))return false; data.Reservations[id]=(r.Qty,"Cancelled"); return true; }
}
