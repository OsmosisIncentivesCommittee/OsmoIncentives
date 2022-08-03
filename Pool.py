from util import *
import Query
import Params

class Pool:
    def __init__(self, pools : Any, pid : int):
        pd = Query.load_pool(pid)
        vol = Query.load_volume(pid)

        self.pools = pools
        self.pid = pid
        self.gauge_ids = Query.load_gauge_ids(pid)

        self.assets = [a["symbol"] for a in pd]
        self.category = categorize(self.assets)
        self.base_pair = self.assets[0]
        self.asset_pair = self.assets[1]
        #FIXME Only does 2 asset pools
        self.pool_ratio = int(pd[0]["liquidity"])/int(pd[1]["liquidity"])/2

#       self.base_yield = Query.load_mintscan_rates(self.base_pair) * self.pool_ratio
#       self.asset_yield = Query.load_mintscan_rates(self.asset_pair) * self.pool_ratio

        self.liquidity = int(pd[0]["liquidity"])

        self.volume = sum([x["value"] for x in vol[-7:]])/7
        self.swap_fee = parse_percent(pd[0]["fees"])
        self.fees_collected = self.volume * self.swap_fee

        external_gauges = Query.load_external_gauges(self.pid)
        self.external_per_day = sum([g["daily_value"] for g in external_gauges.values()])

        self.cache : dict[str, Any] = {}

    def premium_apr(self) -> float:
        return Params.category_premiums[self.category]

    # Share of fees collected by this pool relative to total, KPI purposes only
    def fee_share(self) -> float:
        return self.fees_collected() / self.pools.total_fees_collected

    # APR generated in swap fees by this pool based on the last 7 days, display purposes only
    def swap_apr(self) -> float:
        return (self.fees_collected * 365/self.liquidity)

    # APR provided by external incentives
    def external_apr(self) -> float:
        return self.external_per_day() * 365 / self.liquidity

    # APR that Osmosis will provide to encourage matched incentives.
    def matched_apr(self) -> float:
        if self.pid in Params.matched_pool_ids:
            if "OSMO" in self.assets:
                # FIXME staking apr hardcoded
                return min(self.external_apr , 0.28 * Params.match_multiple_cap)
            return min(self.external_apr , (self.base_yield/self.pool_ratio) * Params.match_multiple_cap_non_osmo, (self.asset_yield/(1-self.pool_ratio)) * Params.match_multiple_cap_non_osmo)

    # Total APR including all bonuses for display, does assume 100% bonded to 14 day and Superfluid taken if available
    def total_apr(self) -> float:
        if self.pid in Params.superfluid:
        # FIXME staking apr hardcoded
            return self.base_yield + self.asset_yield + self.premium_apr + self.swap_apr + self.external_apr + self.matched_apr + (0.28 * (1-Params.superfluid_discount) * self.pool_ratio)
        return self.base_yield + self.asset_yield + self.premium_apr + self.swap_apr + self.external_apr + self.matched_apr

    # APR that Osmosis will attempt to give to the pool in incentives
    def osmo_apr(self) -> float:
        return self.base_yield + self.asset_yield + self.premium_apr + self.matched_apr

    def target_spend(self) -> float:
        return self.liquidity * self.osmo_apr/365

    def target_share(self) -> float:
        # match at least the minimum and at most the maximum specified for this pool
        if self.pid in Params.maximums:
            return min(Params.maximums.get(self.pid,0),max(Params.minimums.get(self.pid,0), self.target_spend() / Params.daily_osmo_spend))
        return max(Params.minimums.get(self.pid,0), self.target_spend() / Params.daily_osmo_spend)

#needs to adjust automatically based on sufficient OSMO
    def adjusted_share(self) -> float:
        return self.target_share

    # Compute the imbalance as the ratio of the target share as compared to the current share
    #   with 0 current share being mapped to an imbalance of 0%, to avoid division by zero
    def imbalance_(self) -> float:
        cs = self.pools.get_current_share(self.gauge_ids)
        if cs > 0:
            return self.target_share() / cs
        else:
            return 0
