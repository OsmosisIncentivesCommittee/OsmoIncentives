from util import load_json

token_data = load_json("https://api-osmosis.imperator.co/tokens/v2/all")

tokens = {x["symbol"] : {"price":float(x["price"]), "denom":x["denom"], "exponent":x["exponent"]} for x in token_data}

denoms = {x["denom"] : x["symbol"] for x in token_data}