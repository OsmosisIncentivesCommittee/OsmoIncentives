from util import *


class Parser:
    _assetlist_url = "https://dashboard-mintscan.s3.ap-northeast-2.amazonaws.com/chains/apr.json"

    _assetlist: dict
    _parsed_rates_by_denom: dict

    async def update(self):
        async with load_json() as client:
            req = await client.get(self._assetlist_url)

        if req.status_code != 200:
            raise Exception("Error parsing assetlist")
        self._assetlist = req.json()

    async def parse(self):
        parsed_rates_by_denom = {}
        for asset in self._assetlist['data']:
            denom = asset['denom']
            stakingAPR = asset['stakingAPR']

            parsed_rates_by_denom[denom] = {
                'denom': denom,
                'apr': stakingAPR
            }
        self._parsed_rates_by_denom = parsed_rates_by_denom

    @property
    def parsed_rates_by_denom(self):
        return self._parsed_rates_by_denom
