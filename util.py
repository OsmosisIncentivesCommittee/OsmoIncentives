import json
import urllib.request
import datetime
from typing import Any, Callable
import Params
import time

def load_json_(url : str) -> Any:
    return json.loads(urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8'))


def cached_call(cache : dict[str, Any], key : str, f : Callable[[],Any]):
    r = cache.get(key)
    if r == None:
        r = f()
        cache[key] = r
    return r


query_cache : dict[str, Any] = {}
def load_json(url : str) -> Any:
    r = query_cache.get(url)
    while r == None:
        try:
            time.sleep(1)
            print("loading url: ", url)
            r = load_json_(url)
            query_cache[url] = r
        except Exception as e:
            print("retrying: ", url, e)
            pass
    return r



def parse_percent(s : str) -> float:
    return float(s[:-1])/100

def parse_start_time(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s[:19],"%Y-%m-%dT%H:%M:%S")

def days_from_now(n : int) -> datetime.datetime:
    return datetime.datetime.now() + datetime.timedelta(days=7)

def write_csv(name : str, lines : list[str]) -> None:
    with open(name, "w+") as f:
        f.write("\n".join(lines))

def read_csv(name : str) -> list[list[str]]:
    with open(name, "r") as f:
        return [x.strip().split(",") for x in f.readlines()]

#Sorts pools into categories based on their constituent assets
def categorize(l : list[str]) -> str:
    (base, asset) = based(l)
    if base == "OSMO":
        if asset[-4:] == "OSMO":
            return "LST"
        if asset[:4] == "OSMO":
            return "LST"
        if asset in Params.Stables:
            return "OSMO_STABLE"
        if asset in Params.Majors:
            return "OSMO_MAJOR"
        else:
            return "OSMO_MINOR"
    # Note: This will recognise LSDs as composability pool too. Would need to revise if any (except stOSMO/OSMO) were incentivised.
    elif base[:4] == asset[:4]:
        if base[:4] in Params.Stables:
            return "COMPOSABILITY"   
        if asset[:4] in Params.Stables:
            return "COMPOSABILITY"
        else:
            return "LST"
    elif base[-4:] == asset[-4:]:
        if base[:4] in Params.Stables:
            return "COMPOSABILITY"   
        if asset[:4] in Params.Stables:
            return "COMPOSABILITY"
        else:
            return "LST"
    elif base in Params.Stables:
        return "STABLE_STABLE"
    else:
        return "NO_CATEGORY_MATCHED"

#Defines what the base pair of the pool is for display and categorisation purposes
def based(l : list[str]) -> tuple[str, str, str]:
    a = l[0]
    b = l[1]
    try:
        c = l[2]
    except IndexError:
        c = "None"
    if a == "OSMO":
        return ("OSMO",b)
    elif b == "OSMO":
        return ("OSMO",a)
    elif a == "USDC":
        return ("USDC",b)
    elif b == "USDC":
        return ("USDC",a)
    elif c == "USDC":
        return ("USDC", "3pool")
    elif a == "BUSD":
        return ("BUSD",b)
    elif b == "BUSD":
        return ("BUSD",a)
    elif a == "USDT":
        return ("USDT",b)
    elif b == "USDT":
        return ("USDT",a)
    elif a == "DAI":
        if c == "IST":
            return ("DAI","3pool")
        return ("DAI",b)
    elif b == "DAI":
        return ("DAI",a)
    elif c == "DAI":
        return ("DAI", "3pool")
    elif a == "ATOM":
        return ("ATOM",b)
    elif b == "ATOM":
        return ("ATOM",a)
    elif a[-4:] == b[-4:]:
        ordering = (a,b)
        shorter, longer = sorted(ordering, key=len)
        return (shorter, longer)
    print("assets not based? : ", l)
    return (a,b)
