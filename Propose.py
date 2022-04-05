import datetime
from util import read_csv
import subprocess

new_gauges = {x[0] : x[1] for x in read_csv("data/new_gauges.csv")}

last_commit_message : str = subprocess.run(["git","log","-l","--pretty=%B"], capture_output=True).stdout.decode("utf-8")

description = """
[Link to sheet displaying this proposal](https://docs.google.com/spreadsheets/d/1A05ELgt-KyMB9pAFvzjKmDcT6UrUorFISeLR64zOoTE/edit?usp=sharing)\n
[Link to auto-updating sheet for upcoming proposal](https://docs.google.com/spreadsheets/d/1_LQIC9KkTRoZjBGAxluCzr2oil4AaUorXSY3QGR9JnI/edit?usp=sharing)\n
[Link to Github implementation of the adjustment process](https://github.com/UnityChaos/OsmoIncentives)\n\n
""" + last_commit_message

cmd = [
    "osmosisd",
    "tx",
    "gov",
    "submit-proposal",
    "update-pool-incentives",
    ",".join(list(new_gauges.keys())),
    ",".join(list(new_gauges.values())),
    "--deposit=0uosmo",
    "--from=temp",
    "--keyring-backend=test",
    '--title="Regular Incentive adjustment for '+ str(datetime.date.today()) +'"',
    '--description="' + description + '"',
    '--chain-id=osmo-test-4', #TODO change to mainnet
    '--gas=999999', #TODO will need money on account for gas fees to auto submit proposals 
    "-y",
]

print("Proposal command to run: ", " ".join(cmd))

subprocess.run(cmd)
