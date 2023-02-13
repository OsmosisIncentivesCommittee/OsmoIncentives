incentivized_pool_ids = [
    1, 2, 3, 5, 7, 9, 15, 42,
    463, 497, 
    573, 577, 584, 586,
    602, 604, 605, 608, 625, 626, 627, 641, 648, 651, 674, 678, 681,
    704, 712, 722, 725, 730, 731, 773, 789, 795, 
    806, 812, 833, 840, 877, 899
    ]

#633, #818, #625, #634, Gravity pools, end approx February 21st 2023
#553 LIKE, end 11th April 2023
#604 STARS, end 12th March 2023

matched_pool_ids = [
    625,
    633,
    634,
    818,
    553,
    604,
    886
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC", "DOT", "WBNB", "WMATIC", "WAVAX"]

Stables = ["USDC", "DAI", "BUSD", "USDT"]

Category_weights = {
    "OSMO_STABLE" : 0.17,
    "STABLE_STABLE" : 0.04,
    "OSMO_MAJOR" : 0.54,
    "OSMO_MINOR" : 0.25,
    "NO_CATEGORY_MATCHED" : 0.01
}

Category_Order = {
    "OSMO_STABLE" : 0,
    "STABLE_STABLE" : 1,
    "OSMO_MAJOR" : 2,
    "OSMO_MINOR" : 3,
    "NO_CATEGORY_MATCHED" : 4.
}

Minimums = {
    9 : 0.02,
    481 : 0.005,
    674 : 0.035,
    704 : 0.10,
    712 : 0.085,
    773 : 0.005,
    899 : 0.005
}

Maximums = {
    1 : 0.35,
    678 : 0.13
}

#Causes Maturity to be overruled, use for 1 proposal when changing minimums or matching incentives to ensure they are met
MaturityExceptions = [
    886,
    899,
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

#Share of the 1, 7 and 14 day gauges
share_1 = 0
share_7 = 0
share_14 = 1

#How accurate is the OSMO weighting allocation
gauge_precision = 100000000

#% of LP emissions redirected to community pool
community_pool_share = 0.70

#Remaining share to split between incentivised pools
total_incentive_share = 1 - community_pool_share
