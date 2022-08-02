from util import *


class Parser:
    _assetlist_url = "https://raw.githubusercontent.com/ToggLeTek/assetlists/main/osmosis-1/osmosis-frontier.assetlist.json"

    _assetlist: dict
    _parsed_assetlist_by_denom: dict

    async def update(self):
        async with load_json() as client:
            req = await client.get(self._assetlist_url)

        if req.status_code != 200:
            raise Exception("Error parsing assetlist")
        self._assetlist = req.json()

    async def parse(self):
        parsed_assetlist_by_denom = {}
        for asset in self._assetlist['assets']:
            denom = asset['base']

            parsed_assetlist_by_denom[denom] = {
                'denom': denom
            }
        self._parsed_assetlist_by_denom = parsed_assetlist_by_denom

    @property
    def parsed_assetlist_by_denom(self):
        return self._parsed_assetlist_by_denom
