from util import *
import Query
import Params

class Pool:
    def __init__(self,pools, pid):
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
        
        self.gauge_ids = Query.load_gauge_ids(pid)

        self.assets = [a["symbol"] for a in pd]
        self.bias = "OSMO" in self.assets and 1+Params.osmo_bias or 1-Params.osmo_bias

        self.cache = {}
    
    # def fee_apr(self):
    #     return 365*self.fees_collected()/self.liquidity

    # def current_incentive_share(self):
    #     return get_current_share(self.gauge_ids)

    # def current_per_day(self):
    #     return self.current_incentive_share() * total_lp_incentives

    # def current_subsidy(self):
    #     return self.current_per_day() / self.fees_collected()

    # def osmo_apr(self):
    #     return 365 * self.current_per_day() / self.liquidity()
    

    # def external_per_day(self):
        
    
    # def external_apr(self):
    #     return 365 * self.external_per_day() / self.liquidity()

    # def is_matched(self):
    #     return self.pid in matched_pool_ids


    
    def unnorm_match_share_(self):
        if self.pid in Params.matched_pool_ids:
            return min(
                self.external_per_day * min(1, self.bias),
                self.bias * self.pools.avg_subsidy() * self.fees_collected #FIXME apply swap fee cap here too
            ) / Query.load_total_lp_spend()
        else:
            return 0
    def unnorm_match_share(self):
        return cached_call(self.cache, "unnorm_match_share", self.unnorm_match_share_)

    
    def match_share_(self):
        return self.pools.match_share_renormalization_factor() * self.unnorm_match_share()
    def match_share(self):
        return cached_call(self.cache, "match_share", self.match_share_)

    
    #Compute the target subsidy as the biased average subsidy plus the match subsidy for this pool
    def target_subsidy_(self):
        match_subsidy = self.match_share() * Query.load_total_lp_spend() / self.fees_collected
        return self.bias * self.pools.avg_subsidy() + match_subsidy
    def target_subsidy(self):
        return cached_call(self.cache, "target_subsidy", self.target_subsidy_)
    
    #Compute the target share as the target subsidy multipled by the relative share of fees collected,
    #   capped at swap_fee_cap multiplied by the avg over all incentivized pools,
    #   then renormalize so that the sum over all target shares is 99% (with 1% for community pool)
    def unnorm_target_share_(self):
        return self.target_subsidy() * min(
            self.fees_collected / Query.load_total_lp_spend(),
            (self.pools.avg_fee_apr() * self.liquidity * Params.swap_fee_cap) / (365 * Query.load_total_lp_spend())
        )
    def unnorm_target_share(self):
        return cached_call(self.cache, "unnorm_target_share", self.unnorm_target_share_)

    def target_share_(self):
        return self.unnorm_target_share() * self.pools.target_renormalization_factor()
    def target_share(self):
        return cached_call(self.cache, "target_share", self.target_share_)

    def imbalance_(self):
        cs = self.pools.get_current_share(self.gauge_ids)
        if cs > 0:
            return self.target_share() / cs
        else:
            return 0
    def imbalance(self):
        return cached_call(self.cache, "imbalance", self.imbalance_)

    def unnorm_scale_limited_target_(self):
        return self.pools.get_current_share(self.gauge_ids) * max(1 - Params.adjust_scale, min(1 + Params.adjust_scale, self.imbalance()))
    def unnorm_scale_limited_target(self):
        return cached_call(self.cache, "unnorm_scale_limited_target", self.unnorm_scale_limited_target_)

    def scale_limited_target_(self):
        return self.unnorm_scale_limited_target() * self.pools.scale_limit_renormalization_factor()
    def scale_limited_target(self):
        return cached_call(self.cache, "scale_limited_target", self.scale_limited_target_)
    
    def unnorm_adjusted_share_(self):
        scale_limit_factor = min(1, self.maturity / Params.entry_window)
        target_factor = max(0, 1 - self.maturity / Params.entry_window)
        return (self.scale_limited_target() * scale_limit_factor) + (self.target_share() * target_factor)
    def unnorm_adjusted_share(self):
        return cached_call(self.cache, "unnorm_adjusted_share", self.unnorm_adjusted_share_)

    def adjusted_share_(self):
        return self.unnorm_adjusted_share() * self.pools.adjustment_renormalization_factor()
    def adjusted_share(self):
        return cached_call(self.cache, "adjusted_share", self.adjusted_share_)
