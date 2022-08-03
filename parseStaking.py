from util import *
import parseDenom

class StakingAPRS:
    staking_url = "https://dashboard-mintscan.s3.ap-northeast-2.amazonaws.com/chains/apr.json"
    
    _stakelist: dict
    _parsed_rates_by_denom: dict
    _parsed_rates_by_symbol: dict
    
    def load_rates():
        staking_data = load_json(staking_url),
        parsed_rates_by_denom = {}

        for asset in staking_data._stakelist['data']:
            denom = asset['denom']
            apr = asset['stakingAPR']
            
            parsed_rates_by_denom[denom] = {
                'denom': denom,
                'apr': apr,
            }
        staking_data._parsed_rates_by_denom = parsed_rates_by_denom
    
    def load_symbols():
        rates = StakingAPRS._parsed_rates_by_denom
        assets = parseDenom.Assets._parsed_assetlist_by_denom

    @property
    def parsed_rates_by_denom(self):
        return self._parsed_rates_by_denom

    @property
    def parsed_rates_by_symbol(self):
        return self._parsed_rates_by_symbol
