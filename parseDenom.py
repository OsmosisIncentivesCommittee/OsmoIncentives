from util import *


class Assets:
    assetlist_url = "https://raw.githubusercontent.com/ToggLeTek/assetlists/main/osmosis-1/osmosis-frontier.assetlist.json"
    
    _assetlist: dict
    _parsed_assetlist_by_denom: dict

    def load_assets():
        asset_data = load_json(assetlist_url),
        parsed_assetlist_by_denom = {}
        for asset in asset_data._assetlist['assets']:
            denom = asset['base']
            symbol = asset['symbol']
            source_denom = asset['denom_units: ["aliases"]']
            for exponent in asset['denom_units: ["exponent"']:
                if symbol.lower() is not asset['denom_units: ["denom"']:
                    exponent = 0
                    return asset['denom_units: ["exponent"']

            parsed_assetlist_by_denom[denom] = {
                'denom': denom,
                'symbol': symbol,
                'source_denom': source_denom,
                'exponent': exponent
            }
        asset_data._parsed_assetlist_by_denom = parsed_assetlist_by_denom

    @property
    def parsed_assetlist_by_denom(self):
        return self._parsed_assetlist_by_denom
