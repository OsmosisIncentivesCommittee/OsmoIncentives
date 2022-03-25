from util import *
import Params

IMPERATOR = "https://api-osmosis.imperator.co/"
BLOCKAPSIS = "https://lcd-osmosis.blockapsis.com/osmosis/"

def load_pool(pid):
    return load_json(IMPERATOR+"pools/v2/"+str(pid))

def load_volume(pid):
    return load_json(IMPERATOR+"pools/v2/volume/"+str(pid)+"/chart")

def load_gauge_ids(pid):
    gs = load_json(BLOCKAPSIS+"pool-incentives/v1beta1/gauge-ids/"+str(pid))["gauge_ids_with_duration"]
    return {g["duration"]:int(g["gauge_id"]) for g in gs}

def load_distr_info():
    return load_json(BLOCKAPSIS+"pool-incentives/v1beta1/distr_info")["distr_info"]

def load_tokens():
    token_data = load_json(IMPERATOR+"tokens/v2/all")
    return {x["symbol"] : {"price":float(x["price"]), "denom":x["denom"], "exponent":x["exponent"]} for x in token_data}

def load_symbols():
    token_data = load_json(IMPERATOR+"tokens/v2/all")
    return {x["denom"] : x["symbol"] for x in token_data}

def load_total_lp_spend():
    daily_osmo_issuance = float(load_json(BLOCKAPSIS+"mint/v1beta1/epoch_provisions")["epoch_provisions"])/1000000
    lp_mint_proportion = float(load_json(BLOCKAPSIS+"mint/v1beta1/params")["params"]["distribution_proportions"]["pool_incentives"])
    return Params.total_incentive_share * daily_osmo_issuance * lp_mint_proportion * load_tokens()["OSMO"]["price"]

#FIXME pagination limits on the gauges query
def load_external_gauges(pid):
    tokens = load_tokens()
    symbols = load_symbols()
    gauges_data = load_json(BLOCKAPSIS+"incentives/v1beta1/gauges")["data"]

    is_external = lambda g: all([
        g["distribute_to"]["denom"] == "gamm/pool/"+str(pid), # paid to this pool
        not g["is_perpetual"],                                # not perpetual (so this math works)
        int(g["num_epochs_paid_over"]) > int(g["filled_epochs"]) + 7,   # won't end in the next week   
        parse_start_time(g["start_time"]) < days_from_now(7),  # started or starts in next week
        len(g["coins"]) == 1 and g["coins"][0]["denom"].startswith("ibc")
        #single asset + ibc assets only for simplicity of lookup (grouped for short circuit)
    ])
        

    external_gauges = {}
    for g in gauges_data:
        if is_external(g):
            denom = g["coins"][0]["denom"]
            symbol = symbols[denom]
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