namespace Challenge;
public record OrderLine(decimal UnitPrice, int Quantity);
public static class Pricing {
 public static decimal Total(string level, IEnumerable<OrderLine> lines, decimal taxRate) {
  var subtotal=lines.Sum(x=>x.UnitPrice*x.Quantity);
  return Math.Round(subtotal*(1+taxRate),2,MidpointRounding.AwayFromZero);
 }
}
