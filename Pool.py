from util import *
import Query
import Params

class Pool:
    def __init__(self, pools : Any, pid : int):
        pd = Query.load_pool(pid)
        vol = Query.load_volume(pid)

        self.pools = pools
        self.pid = pid
        
        self.liquidity = int(pd[0]["liquidity"])
        self.volume = sum([x["value"] for x in vol[-7:]])/7
        self.maturity = min(4, int(len(vol)/7))
        
        self.swap_fee = parse_percent(pd[0]["fees"])
        self.fees_collected = self.volume * self.swap_fee

        external_gauges = Query.load_external_gauges(self.pid)
        self.external_per_day = sum([g["daily_value"] for g in external_gauges.values()])

        # self.adjusted_revenue = self.fees_collected + (se)
        
        self.gauge_ids = Query.load_gauge_ids(pid)

        self.assets = [a["symbol"] for a in pd]
        self.category = categorize(self.assets)

        self.cache : dict[str, Any] = {}


    def adjusted_revenue(self) -> int:
        if self.pid in Params.matched_pool_ids:
            return self.fees_collected + min(self.fees_collected, self.external_per_day)
        return self.fees_collected
    
    def target_share(self) -> float:
        w = Params.Category_weights[self.category]
        ar = self.adjusted_revenue()
        car = self.pools.total_adjusted_revenue_for(self.category)
        return (w * ar) / car 


    #Compute the share of incentives needed to match external incentives on this pool
    #This is only applies if the pool is being matched, and is equal to:
    #   The $ per day of the external incentives applied to this pool,
    #   scaled by capped bias (0.5 for non-osmo pools, 1 for osmo pools)
    #   and capped at the target $ per day for the pool
    # Dividied by the total $ per day of LP incentives
    # def unnorm_match_share_(self) -> float:
    #     if self.pid in Params.matched_pool_ids:
    #         return min(
    #             self.external_per_day * min(1, self.bias),
    #             self.bias * self.pools.avg_subsidy() * self.fees_collected #FIXME apply swap fee cap here too
    #         ) / Query.load_total_lp_spend()
    #     else:
    #         return 0
    # def unnorm_match_share(self) -> float:
    #     return cached_call(self.cache, "unnorm_match_share", self.unnorm_match_share_)

    #We then renormalize the match share, so that it does not exceed the total match limit
    # def match_share_(self) -> float:
    #     return self.pools.match_share_renormalization_factor() * self.unnorm_match_share()
    # def match_share(self) -> float:
    #     return cached_call(self.cache, "match_share", self.match_share_)

    
    #Compute the target subsidy as the biased average subsidy plus the match subsidy for this pool
    # def target_subsidy_(self) -> float:
    #     match_subsidy = self.match_share() * Query.load_total_lp_spend() / self.fees_collected
    #     return self.bias * self.pools.avg_subsidy() + match_subsidy
    # def target_subsidy(self) -> float:
    #     return cached_call(self.cache, "target_subsidy", self.target_subsidy_)
    
    #Compute the target share as the target subsidy multipled by the relative share of fees collected,
    #   capped at swap_fee_cap multiplied by the avg over all incentivized pools,
    # def unnorm_target_share_(self) -> float:
    #     return self.target_subsidy() * min(
    #         self.fees_collected / Query.load_total_lp_spend(),
    #         (self.pools.avg_fee_apr() * self.liquidity * Params.swap_fee_cap) / (365 * Query.load_total_lp_spend())
    #     )
    # def unnorm_target_share(self) -> float:
    #     return cached_call(self.cache, "unnorm_target_share", self.unnorm_target_share_)

    #We then renormalize so that the sum over all target shares is 99% (with 1% for community pool)
    # def target_share_(self) -> float:
    #     return self.unnorm_target_share() * self.pools.target_renormalization_factor()
    # def target_share(self) -> float:
    #     return cached_call(self.cache, "target_share", self.target_share_)

    #Compute the imbbalance as the ratio of the target share as compared to the current share
    #   with 0 current share being mapped to an imbalance of 0%, to avoid division by zero
    def imbalance_(self) -> float:
        cs = self.pools.get_current_share(self.gauge_ids)
        if cs > 0:
            return self.target_share() / cs
        else:
            return 0
    def imbalance(self):
        return cached_call(self.cache, "imbalance", self.imbalance_)

    #Compute the adjustment from the current share, to the target share
    # limited to be no more than the current adjustment scale
    # ie, bounding imbalance between 0.75 and 1.25
    def unnorm_scale_limited_target_(self) -> float:
        return self.pools.get_current_share(self.gauge_ids) * max(1 - Params.adjust_scale, min(1 + Params.adjust_scale, self.imbalance()))
    def unnorm_scale_limited_target(self) -> float:
        return cached_call(self.cache, "unnorm_scale_limited_target", self.unnorm_scale_limited_target_)

    #Then renormalize again so that total scale limited target is 99% of incentives
    def scale_limited_target_(self) -> float:
        return self.unnorm_scale_limited_target() * self.pools.scale_limit_renormalization_factor()
    def scale_limited_target(self) -> float:
        return cached_call(self.cache, "scale_limited_target", self.scale_limited_target_)
    
    #Compute the adjusted share, as the linear average of the target share and the scale limited target
    # based on the maturity level of the pool as compared to the entry window
    # ie linearly shift from entirely the target, to entirely the scale limited target over 4 weeks
    def unnorm_adjusted_share_(self) -> float:
        scale_limit_factor = min(1, self.maturity / Params.entry_window)
        target_factor = max(0, 1 - self.maturity / Params.entry_window)
        return (self.scale_limited_target() * scale_limit_factor) + (self.target_share() * target_factor)
    def unnorm_adjusted_share(self) -> float:
        return cached_call(self.cache, "unnorm_adjusted_share", self.unnorm_adjusted_share_)

    #Then we apply a final renormalization so that again the total of all adjsuted shares is 99%
    def adjusted_share_(self) -> float:
        return self.unnorm_adjusted_share() * self.pools.adjustment_renormalization_factor()
    def adjusted_share(self) -> float:
        return cached_call(self.cache, "adjusted_share", self.adjusted_share_)
