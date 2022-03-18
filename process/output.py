
from util import *
from .calculations import pools
from state.incentivized_pools import pool_onboarding_dates
from .new_gauges import new_gauges

def get_columns(pid):
    p = pools[pid]
    return map(str, [
        pid,
        based(p["assets"])[0],
        based(p["assets"])[1],
        p["liquidity"],
        p["volume"],
        p["swap_fee"],
        p["weekly_fees_collected"],
        p["fee_apr"],
        p["current_incentive_share"],
        p["current_$_per_day"],
        p["current_subsidy"],
        p["osmo_apr"],
        "",#TODO external denom,
        "",#TODO external num,
        "",#TODO external epochs remaining,
        p["external_$_per_day"],
        p["external_apr"],
        p["is_matched"],
        p["match_$_per_day"],
        p["match_share"],
        p["match_subsidy"],
        p["bias"],
        p["target_subsidy"],
        p["target_share"],
        p["imbalance"],
        p["target_limited_by_scaling"],
        pool_onboarding_dates.get(pid,""),
        p["maturity"],
        p["merged_with_maturity"]
    ])

def generate():
    lines = [
        ",".join(get_columns(pid))
        for pid in sorted(pools.keys())]

    write_csv("data/incentives.csv", lines)

    write_csv("data/new_gauges.csv", [str(gid)+","+str(weight) for (gid,weight) in new_gauges.items()])
