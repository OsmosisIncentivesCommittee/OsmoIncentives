from .calculations import pools
from state.params import *


new_gauges = {
    0 : int(gauge_precision * community_pool_share),   
}

for (pid, p) in pools.items():
    new_gauges[p["gauge_ids"]["86400s"]] = int(p["renormalized_share"] * share_1 * gauge_precision)
    new_gauges[p["gauge_ids"]["604800s"]] = int(p["renormalized_share"] * share_7 * gauge_precision)
    new_gauges[p["gauge_ids"]["1209600s"]] = int(p["renormalized_share"] * share_14 * gauge_precision)

