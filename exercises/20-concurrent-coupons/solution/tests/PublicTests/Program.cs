using Challenge;var d=new CouponStore();d.Valid.Add("A");if(!new CouponService(d).Redeem("A"))throw new Exception();Console.WriteLine("Public tests passed");
