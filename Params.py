incentivized_pool_ids = [
    1, 2, 3, 4, 5, 7, 9, 10, 13, 15, 42,
    463, 481, 497, 498,
    573, 577, 584, 585, 586,
    602, 604, 605, 608, 611, 625, 626, 627, 641, 648, 651, 674, 678, 681,
    704, 712, 722, 725, 730, 731, 773, 789, 795, 806, 812, 833, 840
    ]

#722, EVMOS, ends 19th January 2023
#633, #818, #625, #634, Gravity pools, end approx February 21st 2023
#553 LIKE, end 11th April 2023
#604 STARS, end 12th March 2023

matched_pool_ids = [
    722,
    625,
    633,
    634,
    818,
    553,
    604
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC", "DOT", "WBNB", "WMATIC"]

Stables = ["EEUR", "USDC", "DAI"]

Category_weights = {
    "OSMO_MAJOR" : 0.54,
    "OSMO_STABLE" : 0.17,
    "OSMO_MINOR" : 0.25,
    "MAJOR_STABLE" : 0,
    "STABLESWAP" : 0,
    "OTHERS" : 0
}

Category_Order = {
    "OSMO_STABLE" : 0,
    "OSMO_MAJOR" : 1,
    "MAJOR_STABLE" : 2,
    "STABLESWAP" : 3,
    "OSMO_MINOR" : 4,
    "OTHERS" : 5
}

#789, MATIC, Last Proposal dated 9th January 2023 then remove
Minimums = {
    9 : 0.02,
    481 : 0.005,
    674 : 0.035,
    704 : 0.10,
    712 : 0.085,
    773 : 0.005,
    789 : 0.005
}

Maximums = {
    1 : 0.35,
    678 : 0.13,
    498 : 0,
    611 : 0,
    585 : 0,
    4 : 0,
    10 : 0,
    13 : 0
}

#Causes Maturity to be overruled, use for 1 proposal when changing minimums or matching incentives to ensure they are met
MaturityExceptions = [
    498,
    611,
    585,
    4,
    10,
    13
    ]

match_limit = 0.30
adjust_scale = 0.25
entry_window = 4

swap_fee_cap = 3
match_fee_cap_non_osmo = 0.33
match_multiple_cap = 1
match_multiple_cap_non_osmo = 0.5

share_1 = 0.5
share_7 = 0.3
share_14 = 0.2

gauge_precision = 100000000

community_pool_share = 0.70
total_incentive_share = 1 - community_pool_share
