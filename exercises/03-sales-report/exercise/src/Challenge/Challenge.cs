namespace Challenge;
public record Sale(string ProductId,decimal Amount,int Quantity,DateTimeOffset At,string Status);
public record ProductTotal(string ProductId,decimal Revenue,int Quantity);
public static class Reports { public static IReadOnlyList<ProductTotal> Sales(IEnumerable<Sale> sales,DateTimeOffset from,DateTimeOffset to,int skip,int take)=>sales.Where(x=>x.At>=from&&x.At<=to).Skip(skip).Take(take).GroupBy(x=>x.ProductId).Select(g=>new ProductTotal(g.Key,g.Sum(x=>x.Amount),g.Sum(x=>x.Quantity))).OrderByDescending(x=>x.Revenue).ToList(); }
