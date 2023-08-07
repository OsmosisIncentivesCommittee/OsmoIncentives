incentivized_pool_ids = [
    1, 3, 5, 7, 9, 15,
    497, 
    573, 584, 586,
    604, 605, 625, 627, 641, 678, 681,
    704, 712, 722, 725, 730, 773, 789, 795, 
    803, 806, 810, 812, 817, 831, 833, 837, 840, 857, 872, 873, 886, 899, 
    903, 907, 908, 922, 938, 939, 944, 948, 956, 971,
    1011, 1013, 1035, 1039, 1066
    ]
# 1006, FIL, Temporarily Removed from automatic incentives as there has been 0 volume. Incentives will remain the same for the time being due to this.

# 1036 LORE, Matched until Supercharged Pool available
# 1057 PICA, Matched until proposal of 1st July 2024
# 1060 QSR, Matched until proposal of 23rd October 2023
# 882 NOM,  Matched until proposal of 6th November 2023
matched_pool_ids = [
    882, 1036, 1057, 1060
    ]

Majors = ["ATOM", "CRO", "ETH", "WBTC", "DOT", "BNB", "MATIC", "AVAX", "FTM", "FIL", "ARB", "LINK"]

Stables = ["USDC", "DAI", "USDT", "IST", "CMST"]

Category_weights = {
    "OSMO_STABLE" : 0.17,
    "STABLE_STABLE" : 0.04,
    "OSMO_MAJOR" : 0.51,
    "OSMO_MINOR" : 0.23,
    "LST" : 0.05,
    "COMPOSABILITY" : 0.00074,
    "NO_CATEGORY_MATCHED" : 0
}

Category_Order = {
    "OSMO_STABLE" : 0,
    "STABLE_STABLE" : 1,
    "OSMO_MAJOR" : 2,
    "OSMO_MINOR" : 3,
    "LST" : 4,
    "COMPOSABILITY" : 5,
    "NO_CATEGORY_MATCHED" : 6.
}

Minimums = {
    704 : 0.10,
    712 : 0.085
}

# 1 ATOM/OSMO
# 678 USDC/OSMO
Maximums = {
    1 : 0.32,
    678 : 0.13,
    832 : 0,
    960 : 0
}

# 872 USDC.axl/USDC.grv
# 873 USDT.axl/USDT.grv
# 938 polygon.USDC.axl/avalanche.USDC.axl/USDC.axl
Fixed = {
    872 : 0.000211,
    873 : 0.000211,
    938 : 0.000316
}

#Causes Maturity to be overruled, use for 1 proposal when changing minimums or matching incentives to ensure they are met
MaturityExceptions = [
    882, 1060
    ]

# Migration links established by governance. Manually setting for now.
migration_links = {
    1066 : 674
}

collateral_incentives = 0.01

CollateralShare = {
    803 : 1
}

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
community_pool_share = 0

#Remaining share to split between incentivised pools
total_incentive_share = 1 - community_pool_share
