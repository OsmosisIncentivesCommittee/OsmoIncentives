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

        # Combines incentivised pools and externally matched pools only
        all_pools_with_incentives = list(Params.incentivized_pool_ids)
        all_pools_with_incentives.extend(x for x in Params.matched_pool_ids if x not in all_pools_with_incentives)
        all_pools_with_incentives.sort()
        self.pools = {pid : Pool(self, pid) for pid in all_pools_with_incentives}

    def get_current_share(self, gids : dict[str, int]):
        return sum([self.gauge_weights.get(gid,0) for gid in gids.values()])/self.total_weight

    def total_liquidity(self, category : str) -> int:
        return cached_call(self.cache, "total_liquidity", lambda:
            sum([p.liquidity for p in self.pools.values() if category=="" or p.category == category])
        )

    def total_fees(self, category : str) -> int:
        return sum([p.fees_collected for p in self.pools.values() if category=="" or p.category == category])

    def avg_fee_apr(self, category : str) -> float:
        return (365 * self.total_fees(category)) / self.total_liquidity(category)

    def community_pool_share(self, category : str) -> float:
        return 1-sum([p.adjusted_share for p in self.pools.values() if category=="" or p.category == category])

    def new_gauges(self) -> dict[int, int]:
        gs = {0 : int(Params.gauge_precision * self.community_pool_share)}
        for p in self.pools.values():
            new_share = p.adjusted_share()
            gs[p.gauge_ids["86400s"]] = int(new_share * Params.share_1 * Params.gauge_precision)
            gs[p.gauge_ids["604800s"]] = int(new_share * Params.share_7 * Params.gauge_precision)
            gs[p.gauge_ids["1209600s"]] = int(new_share * Params.share_14 * Params.gauge_precision)
        return gs
