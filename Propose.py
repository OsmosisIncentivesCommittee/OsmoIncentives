import datetime
from util import read_csv
import subprocess

new_gauges = {x[0] : x[1] for x in read_csv("data/new_gauges.csv")}

last_commit_message : str = subprocess.run(["git","log","-l","--pretty=%B"], capture_output=True).stdout.decode("utf-8")

description = "\\n".join([
    "[Link to sheet displaying this proposal](https://docs.google.com/spreadsheets/d/1ydQfgEDot0AC9xuT2txc39VBfuum_I1gU_1-GrmrWx4/edit?usp=sharing)",
    "[Link to auto-updating sheet for upcoming proposal](https://docs.google.com/spreadsheets/d/1oEn8JtrIU1mze_3Fw4DbbxWBq6yPUM-yAoaOPxG6Y1k/edit?usp=sharing)",
    "[Link to Github implementation of the adjustment process](https://github.com/OsmosisIncentivesCommittee/OsmoIncentives)",
    last_commit_message])

cmd = [
    "osmosisd",
    "tx",
    "gov",
    "submit-proposal",
    "update-pool-incentives",
    ",".join(list(new_gauges.keys())),
    ",".join(list(new_gauges.values())),
    "--deposit=0uosmo",
    "--from=proposer",
    "--keyring-backend=test",
    '--title=\"Regular Incentive adjustment for '+ str(datetime.date.today()) +'\"',
    '--description=\"' + description + '\"',
    '--chain-id=osmosis-1',
    '--node=https://rpc-osmosis.blockapsis.com:443',
    '--gas=1500000',
    '--gas-prices=0.0025uosmo',
    "-y"
]

print("Proposal command to run: ", " ".join(cmd))

subprocess.run(cmd)
