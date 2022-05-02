from Pool import Pool
import Params
import Query
from util import *

class Pools:
    def __init__(self):
        

        distr_info = Query.load_distr_info()
        self.gauge_weights = {int(r["gauge_id"]) : int(r["weight"]) for r in distr_info["records"]}
        self.total_weight = int(distr_info["total_weight"])
        self.cache : dict[str, Any] = {}

        self.pools = {pid : Pool(self, pid) for pid in Params.incentivized_pool_ids}

    def get_current_share(self, gids : dict[str, int]):
        return sum([self.gauge_weights.get(gid,0) for gid in gids.values()])/self.total_weight

    def total_liquidity(self, category : str) -> int:
        return cached_call(self.cache, "total_liquidity", lambda:
            sum([p.liquidity for p in self.pools.values() if p.category == category])
        )
    
    def total_fees(self, category : str) -> int:
        return sum([p.fees_collected for p in self.pools.values() if p.category == category])
    
    def total_capped_fees(self, category : str) -> int:
        return sum([p.capped_fees() for p in self.pools.values() if p.category == category])

    def avg_fee_apr(self, category : str) -> float:
        return (52 * self.total_fees(category)) / self.total_liquidity(category)

    # def avg_subsidy(self) -> float:
    #     return Query.load_total_lp_spend() / self.total_fees()


    def total_adjusted_revenue_for(self, cat : str) -> int:
        return sum([p.adjusted_revenue() for p in self.pools.values() if p.category == cat])

    # def match_share_renormalization_factor(self) -> float:
    #     return cached_call(self.cache, "match_share_renormalization_factor", lambda:  
    #         min(1, Params.match_limit / sum([p.unnorm_match_share() for p in self.pools.values()]))
    #     )

    # def target_renormalization_factor(self) -> float:
    #     return cached_call(self.cache, "target_renormalization_factor", lambda:
    #         Params.total_incentive_share / sum([p.unnorm_target_share() for p in self.pools.values()])
    #     )

    def scale_limit_renormalization_factor(self) -> float:
        return cached_call(self.cache, "scale_limit_renormalization_factor", lambda:
            Params.total_incentive_share / sum([p.unnorm_scale_limited_target() for p in self.pools.values()])
        )

    def adjustment_renormalization_factor(self) -> float:
        return cached_call(self.cache, "adjusted_renormalization_factor", lambda:
            Params.total_incentive_share / sum([p.unnorm_adjusted_share() for p in self.pools.values()])
        )

    def new_gauges(self) -> dict[int, int]:
        gs = {0 : int(Params.gauge_precision * Params.community_pool_share)}
        for p in self.pools.values():
            new_share = p.adjusted_share()
            gs[p.gauge_ids["86400s"]] = int(new_share * Params.share_1 * Params.gauge_precision)
            gs[p.gauge_ids["604800s"]] = int(new_share * Params.share_7 * Params.gauge_precision)
            gs[p.gauge_ids["1209600s"]] = int(new_share * Params.share_14 * Params.gauge_precision)
        return gs 

