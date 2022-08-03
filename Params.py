incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 15, 42,
    197,
    461, 463, 481, 482, 497, 498,
    549, 553, 557, 571, 573, 577, 584, 585, 586,
    600, 601, 602, 604, 605, 608, 611, 613, 619, 621, 625, 626, 627, 629, 637, 641, 644, 648, 651, 674, 678, 681, 690,
    704, 712, 722, 725, 730, 731, 773
    ]

#577 XKI, Ends 13th August 2022
#600 and 601 CMDX, Ends 10th September 2022
#604 and 611 STARS, Ends 7th October 2022
#648 PSTAKE, Ends 5th August 2022
#690 MNTL, Ends 16th September 2022
#15 and #715, XPRT, Ends 22nd August
#722, EVMOS, ends 18th October 2022
matched_pool_ids = [
    577,
    600, 601,
    604, 611,
    648,
    690,
    15, 719,
    722
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC", "DOT"]

Stables = ["EEUR", "USDC", "DAI"]

# Bonus APR to give to pools in a category
Category_premiums = {
    "OSMO_MAJOR" : 0.05,
    "OSMO_STABLE" : 0.05,
    "OSMO_MINOR" : 0.05,
    "MAJOR_STABLE" : 0,
    "STABLESWAP" : 0,
    "OTHERS" : 0
}

# Order that categories are displayed on the output, the reverse of this is the order in which incentives are drained if there are insufficient to provide target APRs
category_order = {
    "OSMO_STABLE" : 0,
    "OSMO_MAJOR" : 1,
    "MAJOR_STABLE" : 2,
    "STABLESWAP" : 3,
    "OSMO_MINOR" : 4,
    "OTHERS" : 5
}

# Minimum share of LP emissions allocated to a pool to bootstrap liquidity
minimums = {
    1 : 0.15,
    9 : 0.03,
    674 : 0.05,
    704 : 0.10,
    712 : 0.10,
    773 : 0.005
}

# Maximum share of LP emissions available to a pool to prevent over reliance
maximums = {
    1 : 0.25
}

# Caps a base or asset pair's yield at being twice that of an OSMO pair yield
match_yield_cap = 2

# Caps external matching program at X times OSMO APR and Lowest yield APR respectively
match_multiple_cap = 2
match_multiple_cap_non_osmo = 1

# Determines the share of weighting to 1, 7 and 14 day bonded gauges within internal pools
share_1 = 0.5
share_7 = 0.3
share_14 = 0.2

# Accuracy of the weighting split, sufficiently small incentives will not be allocated
gauge_precision = 100000000

# Share of LP emissions to send to the community pool
community_pool_share = 1 - total_incentive_share
