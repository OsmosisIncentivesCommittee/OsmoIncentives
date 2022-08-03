# Explanation of Query.py

## load_pool

> **Variable:** [`IMPERATOR`](https://api-osmosis.imperator.co/swagger/)

![Loaded into Temp Storage](https://img.shields.io/badge/loaded_into-temporary_storage-red)

Loads basic data for the pools mentioned in `Params.py` in sequence.

**Example:**

```json
[
  {
    "symbol": "ATOM",
    "amount": 3637157.533566,
    "denom": "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2",
    "coingecko_id": "cosmos",
    "liquidity": 75081117.33715186,
    "liquidity_24h_change": 3.1964778089588552,
    "volume_24h": 3920844.022423505,
    "volume_24h_change": -23.706563329100796,
    "price": 10.321400247301712,
    "price_24h_change": 4.536698622755016,
    "fees": "0.2%"
  },
  {
    "symbol": "OSMO",
    "amount": 36290030.704378,
    "denom": "uosmo",
    "coingecko_id": "osmosis",
    "liquidity": 75081117.33715186,
    "liquidity_24h_change": 3.1964778089588552,
    "volume_24h": 3920844.022423505,
    "volume_24h_change": -23.706563329100796,
    "price": 1.03445927,
    "price_24h_change": 3.27968904530956,
    "fees": "0.2%"
  }
]
```

## load_volume

> **Variable:** [`IMPERATOR`](https://api-osmosis.imperator.co/swagger/)

![Loaded into Temp Storage](https://img.shields.io/badge/loaded_into-temporary_storage-red)

Loads the **full historical volume** data for the pools mentioned in `Params.py` in sequence. This data is meant to used to *chart* the volume of the pool.

**Example:**

```json
[
  {
    "time": "2021-06-24",
    "value": 17850044
  },
  {
    "time": "2021-06-25",
    "value": 17849676
  },
  {
    "time": "2021-06-26",
    "value": 18504078
  },
  {
    "time": "2021-06-27",
    "value": 20073891
  },
  {
    "time": "2021-06-28",
    "value": 21327195
  },
]
  ```

## load_tokens

> **Variable:** [`IMPERATOR`](https://api-osmosis.imperator.co/swagger/)

![Loaded into Temp Storage](https://img.shields.io/badge/loaded_into-temporary_storage-red)

Loads certain data from the above endpoint. Retrieves:

* `symbol`
* `price` *(as a floating integer)*
  * **Note:** price is `TOKEN/USD`
* `denom`
* `exponent`

**Example *(raw data)*:**

```json
  {
    "price": 0.0298439772,
    "denom": "ibc/987C17B11ABC2B20019178ACE62929FE9840202CE79498E29FE8E5CB02B7C0A4",
    "symbol": "STARS",
    "main": true,
    "liquidity": 2658879.938610659,
    "volume_24h": 80810.480348645,
    "volume_24h_change": -14.2024503623,
    "name": "Stargaze",
    "price_24h_change": 5.4189982145,
    "price_7d_change": 11.1842473232,
    "exponent": 6
  }
  ```

**Example *(parsed)*:**

```json
  {
    "price": 0.0298439772,
    "denom": "ibc/987C17B11ABC2B20019178ACE62929FE9840202CE79498E29FE8E5CB02B7C0A4",
    "symbol": "STARS",
    "exponent": 6
  }
  ```

## load_symbols

> **Variable:** [`IMPERATOR`](https://api-osmosis.imperator.co/swagger/)

![Loaded into Temp Storage](https://img.shields.io/badge/loaded_into-temporary_storage-red)

Loads certain data from the above endpoint and converts it directly into a python `dict`^1. Retrieves:

* `symbol`
* `denom`

This is done so we can know which denom goes with which symbol/ticker.

**Example *(raw data)*:**

```json
  {
    "price": 0.0298439772,
    "denom": "ibc/987C17B11ABC2B20019178ACE62929FE9840202CE79498E29FE8E5CB02B7C0A4",
    "symbol": "STARS",
    "main": true,
    "liquidity": 2658879.938610659,
    "volume_24h": 80810.480348645,
    "volume_24h_change": -14.2024503623,
    "name": "Stargaze",
    "price_24h_change": 5.4189982145,
    "price_7d_change": 11.1842473232,
    "exponent": 6
  }
  ```

**Example *(parsed)*:**

```py
["ibc/987C17B11ABC2B20019178ACE62929FE9840202CE79498E29FE8E5CB02B7C0A4" : "STARS"]
  ```

^[1]: Python `dict`'s are primarily utilized as `key:value` stores, as is the case here.
