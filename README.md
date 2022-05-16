# Osmosis Incentives

This repository contains the code and data needed to implement the currently approved Osmosis incentives process. It also acts as a way to track changes to this process over time.

The main branch contains the process and data for the most recent proposal.

The staging branch contains the process for the next proposal.

Throughout the week, PRs are made to staging corresponding to on chain text proposals, such as adding pools to onboarding, matching external incentives, or changing the adjustment process.

A view branch off of staging is continually updated with new data, so that we can see what we expect the next proposal to look like.

As on chain text proposals pass, their PRs are merged to staging (and then merged to the view branch).

When it's time for a new adjustment proposal, the view branch is merged back into staging (giving it up to date market data). And the staging branch is then merged into main (with the commit message documenting the set of changes since the last adjustment proposal).

The data in the main branch is then used to create the on chain adjustment proposal.


## Project Structure

- Params.py - Values set via text proposals, such as parameters (scale limit, matching limit, etc.), incentivized pool IDs and matched externals.
- Query.py - Functions to get data from Blockapsis and Imperator APIs
- Pools.py/Pool.py - Methods to do the calculations and generate csvs / proposal data
- Update.py - Code to update csv files with new data/calculations
- data/ - csv outputs which are auto imported into [Current Proposal](https://docs.google.com/spreadsheets/d/1ydQfgEDot0AC9xuT2txc39VBfuum_I1gU_1-GrmrWx4/edit?usp=sharing) and [Prospective Proposal](https://docs.google.com/spreadsheets/d/1oEn8JtrIU1mze_3Fw4DbbxWBq6yPUM-yAoaOPxG6Y1k/edit?usp=sharing) spreadsheets and which are used to generate a proposal
- Propose.py - Takes `data/new_gauges.csv` and generates and submits an onchain poolincentives proposal

## Current Incentives Calculation

- external incentives matching
- biased subsidy targets
- scale limiting
- maturity based scale bypass
