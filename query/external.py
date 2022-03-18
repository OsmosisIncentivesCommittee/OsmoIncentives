from util import load_json
from .tokens import *
from state.matched_pools import matched_pool_ids

gauges_data = load_json("https://lcd-osmosis.blockapsis.com/osmosis/incentives/v1beta1/gauges")["data"]

is_external = lambda g: len(g["coins"]) > 0 and \
    (all([c != "uosmo" for c in g["coins"]])) and \
    (not g["is_perpetual"]) and \
    g["distribute_to"]["denom"].startswith("gamm/pool/") and \
    g["num_epochs_paid_over"] != g["filled_epochs"]

external_gauges = {g["id"] : {
    "pool_id" : int(g["distribute_to"]["denom"].split("/")[2]),
    "symbol" : denoms[g["coins"][0]["denom"]],
    "amount" : int(g["coins"][0]["amount"])/pow(10,tokens[denoms[g["coins"][0]["denom"]]]["exponent"]),
    "start_time" : g["start_time"],
    "num_epochs_paid_over" : int(g["num_epochs_paid_over"]),
    "filled_epochs" : int(g["filled_epochs"])
} for g in gauges_data if is_external(g)}

for (gid,g) in external_gauges.items():
    g["daily_value"] = g["amount"]*tokens[g["symbol"]]["price"]/g["num_epochs_paid_over"]
    g["epochs_remaining"] = g["num_epochs_paid_over"]-g["filled_epochs"]
    # g["is_matched"] = g["pool_id"] in matched_pool_ids

