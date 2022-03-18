import json
import urllib.request
import datetime

load_json = lambda url: json.loads(urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8'))

parse_percent = lambda s: float(s[:-1])/100

parse_date =  lambda s: datetime.datetime.strptime(s,"%m/%d/%Y").date()

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
    