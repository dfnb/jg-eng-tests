namespace Challenge;
public record OrderLine(decimal UnitPrice, int Quantity);
public static class Pricing {
 public static decimal Total(string level, IEnumerable<OrderLine> lines, decimal taxRate) {
  var subtotal=lines.Sum(x=>x.UnitPrice*x.Quantity);
  var rate=level.ToUpperInvariant() switch { "GOLD"=>.10m, "SILVER"=>.05m, _=>0m };
  return Math.Round(subtotal*(1-rate)*(1+taxRate),2,MidpointRounding.AwayFromZero);
 }
}
