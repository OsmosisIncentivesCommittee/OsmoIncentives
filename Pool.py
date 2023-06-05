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
        self.gauge_ids = Query.load_gauge_ids(pid)
        
        self.collateral_share = Params.CollateralShare.get(self.pid,0)   
        
        self.swap_fee = parse_percent(pd[0]["fees"])
        self.fees_collected = self.volume * self.swap_fee

        external_gauges = Query.load_external_gauges(self.pid)
        self.external_per_day = sum([g["daily_value"] for g in external_gauges.values()])

        self.assets = [a["symbol"] for a in pd]
        if self.pid == 1006:
            self.assets = ["OSMO","FIL"]
        if self.pid == 1011:
            self.assets = ["OSMO","ARB"]
        if self.pid == 704:
            self.assets = ["OSMO","ETH"]
        if self.pid == 840:
            self.assets = ["OSMO","BNB"]
        if self.pid == 900:
            self.assets = ["OSMO","FTM"]
        if self.pid == 899:
            self.assets = ["OSMO","AVAX"]
        if self.pid == 789:
            self.assets = ["OSMO","MATIC"]
        if self.pid == 1035:
            self.assets = ["UMEE","stUMEE"]
        self.category = categorize(self.assets)
        
        self.cache : dict[str, Any] = {}

        #StableSwap Incentives are not affected by Maturity, otherwise maturity is weeks since listing on info site
        if "STABLE_STABLE" in self.category:
            self.maturity = 0
        else:
            self.maturity = self.pools.get_current_share(self.gauge_ids) != 0 and min(4, int(len(vol)/7)) or 0

    #cap swap fees collected at a multiple of avg per unit tvl to disincentivize wash trading
    def capped_fees(self) -> int:
        if "STABLE_STABLE" in self.category:
            return self.fees_collected
        else:
            return min(self.fees_collected, Params.swap_fee_cap * self.pools.avg_fee_apr(self.category) * self.liquidity)

    #share of fees collected by this pool relative to category total
    def fee_share(self) -> float:
        return self.capped_fees() / self.pools.total_capped_fees(self.category)

    #add capped share of external $ per day to capped fees to calculate adjusted revenue
    def adjusted_revenue(self) -> int:
        if "OSMO" in self.category:
            #Matched but not incentivized
            if self.pid in Params.matched_pool_ids and self.pid not in Params.incentivized_pool_ids:
                return min(self.external_per_day,self.capped_fees())
            #Matched and incentivized
            elif self.pid in Params.matched_pool_ids:
                return self.capped_fees()+min(self.external_per_day,self.capped_fees())
            #Incentivized
            else:
                return self.capped_fees()
        elif "LST" in self.category:
            if self.external_per_day/Query.OSMOPrice > 50:
                return min(self.external_per_day,self.capped_fees())
            else:
                return 0
        else:
            #Matched but not incentivized
            if self.pid in Params.matched_pool_ids and self.pid not in Params.incentivized_pool_ids:
                return min(self.external_per_day*Params.match_multiple_cap_non_osmo,Params.match_fee_cap_non_osmo*self.capped_fees())
            #Matched and incentivized
            elif self.pid in Params.matched_pool_ids:
                return self.capped_fees()+min(self.external_per_day*Params.match_multiple_cap_non_osmo,Params.match_fee_cap_non_osmo*self.capped_fees())
            #Incentivized
            else:
                return self.capped_fees()

    #share of adjusted revenue collected by the pool relative to category total
    def adjusted_revenue_share(self) -> float:
        return self.adjusted_revenue() / self.pools.total_adjusted_revenue_for(self.category)

    #cap adjusted revenue share at 1+MMC of fee share (currently 2x original share)
    def match_capped_share(self) -> float:
        return min((1+Params.match_multiple_cap)*self.fee_share(), self.adjusted_revenue_share())

    #translate category share to overall incentives share
    def target_share(self) -> float:
        #TODO Enable maximums
        if "STABLE_STABLE" in self.category:
            if self.pid in Params.Maximums:
                return min(Params.Maximums.get(self.pid,0) * Params.total_incentive_share,max(Params.Minimums.get(self.pid,0) * Params.total_incentive_share, self.fees_collected*2/(Query.OSMOPrice * Query.daily_osmo_issuance * Query.lp_mint_proportion)))
            else:
                return max(Params.Minimums.get(self.pid,0) * Params.total_incentive_share, self.fees_collected*2/(Query.OSMOPrice * Query.daily_osmo_issuance * Query.lp_mint_proportion))
        elif "NO_CATEGORY_MATCHED" in self.category:
            if self.pid in Params.Maximums:
                return min(Params.Maximums.get(self.pid,0) * Params.total_incentive_share,max(Params.Minimums.get(self.pid,0) * Params.total_incentive_share, self.adjusted_revenue()/(Query.OSMOPrice * Query.daily_osmo_issuance * Query.lp_mint_proportion)))
            else:
                return max(Params.Minimums.get(self.pid,0) * Params.total_incentive_share, self.adjusted_revenue()/(Query.OSMOPrice * Query.daily_osmo_issuance * Query.lp_mint_proportion))
        elif "LST" in self.category:
            if self.pid in Params.Maximums:
                return min(Params.Maximums.get(self.pid,0),max(Params.Minimums.get(self.pid,0), (Params.Category_weights[self.category] - Params.collateral_incentives) * self.match_capped_share() + Params.collateral_incentives * self.collateral_share) * Params.total_incentive_share)
            else:
                return max(Params.Minimums.get(self.pid,0), (Params.Category_weights[self.category] - Params.collateral_incentives) * self.match_capped_share() + Params.collateral_incentives * self.collateral_share) * Params.total_incentive_share
        elif "COMPOSABILITY" in self.category:
            return Params.Fixed.get(self.pid,0)
        elif self.pid in Params.Maximums:
            return min(Params.Maximums.get(self.pid,0),max(Params.Minimums.get(self.pid,0), Params.Category_weights[self.category] * self.match_capped_share())) * Params.total_incentive_share
        return max(Params.Minimums.get(self.pid,0), Params.Category_weights[self.category] * self.match_capped_share()) * Params.total_incentive_share

    #Compute the imbalance as the ratio of the target share as compared to the current share
    #with 0 current share being mapped to an imbalance of 0%, to avoid division by zero
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
        if self.pid in Params.MaturityExceptions:
            return self.target_share()
        elif "STABLE_STABLE" in self.category:
            return self.target_share()
        else:
            scale_limit_factor = min(1, self.maturity / Params.entry_window)
            target_factor = max(0, 1 - self.maturity / Params.entry_window)
            return (self.scale_limited_target() * scale_limit_factor) + (self.target_share() * target_factor)
    def unnorm_adjusted_share(self) -> float:
        return cached_call(self.cache, "unnorm_adjusted_share", self.unnorm_adjusted_share_)

    #Then we apply a final renormalization so that again the total of all adjusted shares is the same as the current emissions to LPs
    def adjusted_share_(self) -> float:
        return self.unnorm_adjusted_share() * self.pools.adjustment_renormalization_factor()
    def adjusted_share(self) -> float:
        return cached_call(self.cache, "adjusted_share", self.adjusted_share_)
