namespace Challenge;
public record Sale(string ProductId,decimal Amount,int Quantity,DateTimeOffset At,string Status);
public record ProductTotal(string ProductId,decimal Revenue,int Quantity);
public static class Reports { public static IReadOnlyList<ProductTotal> Sales(IEnumerable<Sale> sales,DateTimeOffset from,DateTimeOffset to,int skip,int take){if(skip<0||take<=0)throw new ArgumentOutOfRangeException();return sales.Where(x=>x.Status=="Completed"&&x.At>=from&&x.At<to).GroupBy(x=>x.ProductId).Select(g=>new ProductTotal(g.Key,g.Sum(x=>x.Amount),g.Sum(x=>x.Quantity))).OrderByDescending(x=>x.Revenue).ThenBy(x=>x.ProductId,StringComparer.Ordinal).Skip(skip).Take(take).ToList();} }
