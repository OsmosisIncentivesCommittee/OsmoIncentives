incentivized_pool_ids = [
    1, 2, 3, 5, 7, 9, 15, 42,
    497, 
    573, 577, 584, 586,
    602, 604, 605, 608, 625, 626, 627, 641, 648, 651, 674, 678, 681,
    704, 712, 722, 725, 730, 731, 773, 789, 795, 
    806, 812, 831, 833, 837, 840, 857, 872, 873, 899, 
    900, 907, 908, 938, 939, 960, 971, 
    1006, 1011
    ]

# 604 STARS, Ends with proposal of 24th July (Loaded 4 weeks late in error, preapprove 4 week further matching)
# 832 JKL, Ends with proposal of 31st July (3 month period)
matched_pool_ids = [
    604, 832
    ]

Majors = ["ATOM", "CRO", "ETH", "WBTC", "DOT", "BNB", "MATIC", "AVAX", "FTM", "FIL", "ARB", "LINK"]

Stables = ["USDC", "DAI", "USDT", "IST", "CMST"]

Category_weights = {
    "OSMO_STABLE" : 0.17,
    "STABLE_STABLE" : 0.04,
    "OSMO_MAJOR" : 0.54,
    "OSMO_MINOR" : 0.25,
    "COMPOSABILITY" : 0.00074,
    "NO_CATEGORY_MATCHED" : 0
}

Category_Order = {
    "OSMO_STABLE" : 0,
    "STABLE_STABLE" : 1,
    "OSMO_MAJOR" : 2,
    "OSMO_MINOR" : 3,
    "COMPOSABILITY" : 4,
    "NO_CATEGORY_MATCHED" : 5.
}

# 1011 ARB/OSMO, Ends with Proposal of 12th June
Minimums = {
    9 : 0.02,
    674 : 0.035,
    704 : 0.10,
    712 : 0.085,
    773 : 0.005,
    1011 : 0.005
}

# 1 ATOM/OSMO
# 678 USDC/OSMO
Maximums = {
    1 : 0.35,
    678 : 0.13,
    960 : 0
}

# 872 USDC.axl/USDC.grv
# 873 USDT.axl/USDT.grv
# 938 polygon.USDC.axl/avalanche.USDC.axl/USDC.axl
Fixed = {
    872 : 0.0000632,
    873 : 0.0000632,
    938 : 0.0000948
}

#Causes Maturity to be overruled, use for 1 proposal when changing minimums or matching incentives to ensure they are met
MaturityExceptions = [
    960
    ]

#% of Osmo Incentives allowed to be used for External Matching
match_limit = 0.30

#% that the amount of OSMO incentives a pool receives may change by per week
adjust_scale = 0.25

#Weeks since token listing that a token may change incentives more than the adjust_scale cap
entry_window = 4

#Caps the amount of swap fees that can be used to increase the incentives of a pool to X * average swap fee % to prevent excessive volume during the maturing period
swap_fee_cap = 3

#Requires 3x more fees to generate the same incentive matching in non-OSMO Pools
match_fee_cap_non_osmo = 0.33

#Caps the matching externals in OSMO pools at X times the native OSMO APR
match_multiple_cap = 1

#Caps the matching externals in non-OSMO pools at X times the native OSMO APR
match_multiple_cap_non_osmo = 0.5

#How accurate is the OSMO weighting allocation
gauge_precision = 100000000

#% of LP emissions redirected to community pool
community_pool_share = 0.70

#Remaining share to split between incentivised pools
total_incentive_share = 1 - community_pool_share
