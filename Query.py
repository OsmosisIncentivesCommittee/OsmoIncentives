from util import *
import Params
from typing import Any, Callable

IMPERATOR = "https://api-osmosis.imperator.co/"
BLOCKAPSIS = "https://lcd-osmosis.blockapsis.com/osmosis/"

daily_osmo_issuance = float(load_json(BLOCKAPSIS+"mint/v1beta1/epoch_provisions")["epoch_provisions"])/1000000
OSMOPrice = float(load_json(IMPERATOR+"tokens/v2/osmo")[0]["price"])
lp_mint_proportion = float(load_json(BLOCKAPSIS+"mint/v1beta1/params")["params"]["distribution_proportions"]["pool_incentives"])

def load_pool(pid : int):
    return load_json(IMPERATOR+"pools/v2/"+str(pid))

def load_volume(pid : int):
    return load_json(IMPERATOR+"pools/v2/volume/"+str(pid)+"/chart")

def load_gauge_ids(pid : int) -> dict[str, int]:
    gs = load_json(BLOCKAPSIS+"pool-incentives/v1beta1/gauge-ids/"+str(pid))["gauge_ids_with_duration"]
    return {g["duration"]:int(g["gauge_id"]) for g in gs}

def load_distr_info():
    return load_json(BLOCKAPSIS+"pool-incentives/v1beta1/distr_info")["distr_info"]

def load_tokens():
    token_data = load_json(IMPERATOR+"tokens/v2/all")
    return {x["symbol"] : {"price":float(x["price"]), "denom":x["denom"], "exponent":x["exponent"]} for x in token_data}

def load_symbols() -> dict[str, str]:
    token_data = load_json(IMPERATOR+"tokens/v2/all")
    return {x["denom"] : x["symbol"] for x in token_data}

def load_total_lp_spend() -> float:
    return daily_osmo_issuance * lp_mint_proportion * OSMOPrice

#FIXME pagination limits on the gauges query, pagination limit kicked in and hid older gauges, should be fine to return to no pagination in September
def load_external_gauges(pid : int) -> dict[str, Any]:
    tokens = load_tokens()
    symbols = load_symbols()
    gauges_data = load_json(BLOCKAPSIS+"incentives/v1beta1/gauges?pagination.limit=25000")["data"]

    is_external : Callable[[dict[str, Any]],bool] = lambda g: all([
        g["distribute_to"]["denom"] == "gamm/pool/"+str(pid), # paid to this pool
        not g["is_perpetual"],                                # not perpetual (so this math works)
        int(g["num_epochs_paid_over"]) > int(g["filled_epochs"]) + 7,   # won't end in the next week
        parse_start_time(g["start_time"]) < days_from_now(7),  # started or starts in next week
        len(g["coins"]) == 1
    ])


    external_gauges : dict[str, Any] = {}
    for g in gauges_data:
        if is_external(g):
            denom = g["coins"][0]["denom"]
            symbol = symbols.get(denom,None)
            if symbol == None:
                continue
            exponent = tokens[symbol]["exponent"]
            amount = int(g["coins"][0]["amount"])/pow(10, exponent)
            price = tokens[symbol]["price"]
            epochs = int(g["num_epochs_paid_over"])
            filled_epochs = int(g["filled_epochs"])

            external_gauges[g["id"]] = {
                "symbol" : symbol,
                "amount" : amount,
                "start_time" : g["start_time"],
                "epochs": epochs,
                "filled_epochs" : filled_epochs,
                "epochs_remaining" : epochs - filled_epochs,
                "daily_value" : amount * price / epochs
            }
    return external_gauges