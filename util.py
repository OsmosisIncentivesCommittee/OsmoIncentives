import json
import urllib.request
import datetime

load_json_ = lambda url: json.loads(urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8'))


def cached_call(cache, key, f):
    r = cache.get(key)
    if r == None:
        r = f()
        cache[key] = r
    return r


query_cache = {}
def load_json(url):
    r = query_cache.get(url)
    while r == None:
        try:
            print("loading url: ", url)
            r = load_json_(url)
            query_cache[url] = r
        except:
            print("retrying: ", url)
            pass
    return r



parse_percent = lambda s: float(s[:-1])/100

# parse_date =  lambda s: datetime.datetime.strptime(s,"%m/%d/%Y").date()
parse_start_time = lambda s: datetime.datetime.strptime(s[:19],"%Y-%m-%dT%H:%M:%S")
days_from_now = lambda n: datetime.datetime.now() + datetime.timedelta(days=7)

def write_csv(name, lines):
    with open(name, "w") as f:
        f.write("\n".join(lines))

def read_csv(name):
    with open(name, "r") as f:
        return [x.strip().split(",") for x in f.readlines()]

def based(l):
    a = l[0]
    b = l[1]
    if a == "OSMO":
        return ("OSMO",b)
    elif b == "OSMO":
        return ("OSMO",a)
    elif a == "ATOM":
        return ("ATOM",b)
    elif b == "ATOM":
        return ("ATOM",a)
    elif a == "UST":
        return ("UST", b)
    elif b == "UST":
        return ("UST", a)
    elif a == "EEUR":
        return ("EEUR", b)
    elif b == "EEUR":
        return ("EEUR", a)
    print("assets not based? : ", l)
    