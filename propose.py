
#generate a the gaugeid/weight pairs for a command, compare to live sheet
import datetime
from util import read_csv

new_gauges = {x[0] : x[1] for x in read_csv("data/new_gauges.csv")}

description = """
[Link to sheet displaying this proposal](todo.xyz)\n
[Link to auto-updating sheet for upcoming proposal](todo.xyz)\n
[Link to Github implementation of the adjustment process](todo.xyz)\n\n

"""

    #TODO
    # description should have:
    # static - link to "current proposal sheet"
    # static - link to "live updating / next proposal sheet"
    # static - link to repo
    # dynamic - text of most recent commit to main

cmd = " ".join([
    "osmosisd",
    "tx",
    "gov",
    "submit-proposal",
    "update-pool-incentives",
    ",".join(list(new_gauges.keys())),
    ",".join(list(new_gauges.values())),
    "--chain-id=osmosis-1",
    "--deposit=0uosmo",
    "--from=osmosis",
    '--title="Regular Incentive adjustment for '+ str(datetime.date.today()) +'"',
    '--description="' + description + '"',


])

print(cmd)

#TODO use subprocess to execute the command
