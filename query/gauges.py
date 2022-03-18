from util import load_json
from state.params import community_pool_share


distr_info = load_json("https://lcd-osmosis.blockapsis.com/osmosis/pool-incentives/v1beta1/distr_info")["distr_info"]
total_weight = int(distr_info["total_weight"])
gauge_weights = {int(r["gauge_id"]) : int(r["weight"]) for r in distr_info["records"]}

get_gauge_ids = lambda pid: {g["duration"]:int(g["gauge_id"]) for g in load_json("https://lcd-osmosis.blockapsis.com/osmosis/pool-incentives/v1beta1/gauge-ids/"+str(pid))["gauge_ids_with_duration"]}

get_current_share = lambda gids: sum([gauge_weights.get(gid,0) for gid in gids.values()])/total_weight

total_incentive_share = 1 - community_pool_share