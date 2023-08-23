incentivized_pool_ids = [
    1,
    678, 681,
    704, 722, 725, 789, 
    803, 810, 817, 831, 833, 840, 872, 873, 886, 899, 
    903, 908, 922, 938, 939, 944, 948, 956,
    1011, 1035, 1066,
    1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099,
    1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113
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
    1090 : 0.085
}

# 1 ATOM/OSMO
# 678 USDC/OSMO
Maximums = {
    1 : 0.32,
    678 : 0.13
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
    ]

# Migration links established by governance. Manually setting for now.
migration_links = {
    1066 : 674,
    1088 : 837,
    1089 : 857,
    1090 : 712,
    1091 : 773,
    1092 : 9,
    1093 : 3,
    1094 : 812,
    1095 : 584,
    1096 : 604,
    1097 : 497,
    1098 : 806,
    1099 : 907,
    1100 : 1013,
    1101 : 15,
    1102 : 586,
    1103 : 627,
    1104 : 795,
    1105 : 730,
    1106 : 7,
    1107 : 1039,
    1108 : 5,
    1109 : 573,
    1110 : 641,
    1111 : 605 ,
    1112 : 971,
    1113 : 625    
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
