from query.pool_data import pools

from math import ceil
from datetime import date

from util import *
from state.incentivized_pools import *
from state.matched_pools import matched_pool_ids
from state.params import *

from query.gauges import *
from query.external import external_gauges
from query.totals import total_lp_incentives


for (pid,p) in pools.items():
    p["weekly_fees_collected"] = p["volume"]*p["swap_fee"]
    p["fee_apr"] = 52 * p["weekly_fees_collected"]/p["liquidity"]
    p["current_incentive_share"] = get_current_share(p["gauge_ids"])
    p["current_$_per_day"] = p["current_incentive_share"] * total_lp_incentives
    p["current_subsidy"] = 7 * p["current_$_per_day"] / p["weekly_fees_collected"]
    p["osmo_apr"] = 365 * p["current_$_per_day"] / p["liquidity"]

    p["external_$_per_day"] = sum([g["daily_value"] for g in external_gauges.values() if g["pool_id"]==pid])
    p["external_apr"] = 365* p["external_$_per_day"] / p["liquidity"]
    p["is_matched"] = pid in matched_pool_ids

total_liquidity = sum(p["liquidity"] for p in pools.values())
print("total liquidity: ", total_liquidity)

total_fees = sum([p["weekly_fees_collected"] for p in pools.values()])
print("total fees:", total_fees)

avg_fee_apr = (52 * total_fees) / total_liquidity
print("avg fee apr: ", avg_fee_apr)

total_match = sum([p["external_$_per_day"] for p in pools.values() if p["is_matched"]])
print("total match:", total_match)

total_incentives_spend = total_lp_incentives * total_incentive_share
print("total incentives spend :", total_incentives_spend)

match_limit_adjustment = min(1, total_lp_incentives * match_limit / total_match)
print("match limit adjustment:", match_limit_adjustment)

avg_subsidy = (total_incentives_spend * 7) / total_fees
print("avg subsidy:", avg_subsidy)

for (pid,p) in pools.items():
    p["bias"] = "OSMO" in p["assets"] and 1+osmo_bias or 1-osmo_bias
    p["match_$_per_day"] = p["is_matched"] and min(p["external_$_per_day"] * match_limit_adjustment * min(1,p["bias"]), p["bias"]*avg_subsidy*p["weekly_fees_collected"]/7) or 0

    p["match_share"] = p["match_$_per_day"] / total_lp_incentives
    p["match_subsidy"] = p["match_$_per_day"]*7/p["weekly_fees_collected"]

total_match_share = sum([p["match_share"] for p in pools.values()])
print("total match share: ", total_match_share)



for (pid,p) in pools.items():
    
    p["target_subsidy"] = (1-total_match_share)*p["bias"]*avg_subsidy + p["match_subsidy"]
    
    p["target_share"] = p["target_subsidy"] * min(
        p["weekly_fees_collected"]/(7*total_incentives_spend),
        (avg_fee_apr*p["liquidity"]*swap_fee_cap)/(365*total_incentives_spend))

    p["imbalance"] = p["current_incentive_share"] > 0 and p["target_share"]/p["current_incentive_share"] or 1
    p["target_limited_by_scaling"] = p["current_incentive_share"]*max(1-adjust_scale,min(1+adjust_scale,p["imbalance"]))

    p["maturity"] = min(4, int(ceil((date.today() - pool_onboarding_dates.get(pid, parse_date("1/1/0001"))).days / 7.0)))
    p["merged_with_maturity"] = max(p["target_limited_by_scaling"]*min(1,p["maturity"]/entry_window) + p["target_share"]*max(0, 1 - p["maturity"]/entry_window), p["match_share"])
    
pre_renormalized_total = sum([p["merged_with_maturity"] for p in pools.values()])

for (pid,p) in pools.items():
    p["renormalized_share"] = p["merged_with_maturity"] * (total_incentive_share / pre_renormalized_total)
