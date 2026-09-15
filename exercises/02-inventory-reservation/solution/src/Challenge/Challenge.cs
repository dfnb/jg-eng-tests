namespace Challenge;
public sealed class Inventory { public int Available; public Dictionary<string,(int Qty,string State)> Reservations=new(); internal object Gate=new(); }
public sealed class ReservationService(Inventory data) {
 public bool Reserve(string id,int qty){lock(data.Gate){if(qty<=0||data.Available<qty||data.Reservations.ContainsKey(id))return false;data.Available-=qty;data.Reservations[id]=(qty,"Active");return true;}}
 public bool Cancel(string id){lock(data.Gate){if(!data.Reservations.TryGetValue(id,out var r)||r.State!="Active")return false;data.Reservations[id]=(r.Qty,"Cancelled");data.Available+=r.Qty;return true;}}
}
