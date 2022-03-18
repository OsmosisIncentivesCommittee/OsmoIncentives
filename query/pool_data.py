from util import *
from state.incentivized_pools import *
from .gauges import *

all_pools = load_json("https://api-osmosis.imperator.co/pools/v2/all?low_liquidity=false")

#TODO switch this to use /pools/v2/{pool_id} and /pools/v2/volume/{pool_id}/chart
#And take the avg of the last 7 days

pools_data = {pid : all_pools[str(pid)] for pid in incentivized_pool_ids}

pools = {pid : {
    "liquidity" : int(pools_data[pid][0]["liquidity"]),
    "volume" : int(pools_data[pid][0]["volume_7d"]),
    "swap_fee" : parse_percent(pools_data[pid][0]["fees"]),
    "gauge_ids" : get_gauge_ids(pid),
    "assets" : [a["symbol"] for a in pools_data[pid]]
    } for pid in incentivized_pool_ids}

