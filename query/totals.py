from util import load_json
from .tokens import tokens

daily_osmo_issuance = float(load_json("https://lcd-osmosis.blockapsis.com/osmosis/mint/v1beta1/epoch_provisions")["epoch_provisions"])/1000000

lp_incentives_share = float(load_json("https://lcd-osmosis.blockapsis.com/osmosis/mint/v1beta1/params")["params"]["distribution_proportions"]["pool_incentives"])

total_lp_incentives = daily_osmo_issuance * lp_incentives_share * tokens["OSMO"]["price"]