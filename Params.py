incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 15, 42,
    197,
    461, 463, 481, 482, 497, 498,
    549, 553, 557, 571, 573, 577, 584, 585, 586,
    602, 604, 605, 608, 611, 613, 619, 621, 625, 626, 627, 637, 641, 644, 648, 651, 674, 678, 681,
    704, 712, 722, 725, 730, 731, 773, 795, 806, 812, 833, 840
    ]

#837 IST, ends 6th January 2023
#722, EVMOS, ends 19th January 2023
#633, #818, #625, #634, Gravity pools, end approx February 21st 2023
#553 LIKE, end 11th April 2023
#604 STARS, end 12th March 2023
#611 STARS, end 31st January 2023

matched_pool_ids = [
    722,
    625,
    633,
    634,
    818,
    553,
    837,
    604,
    611
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC", "DOT", "WBNB"]

Stables = ["EEUR", "USDC", "DAI"]

Category_weights = {
    "OSMO_MAJOR" : 0.45,
    "OSMO_STABLE" : 0.30,
    "OSMO_MINOR" : 0.14,
    "MAJOR_STABLE" : 0,
    "STABLESWAP" : 0,
    "OTHERS" : 0.02
}

Category_Order = {
    "OSMO_STABLE" : 0,
    "OSMO_MAJOR" : 1,
    "MAJOR_STABLE" : 2,
    "STABLESWAP" : 3,
    "OSMO_MINOR" : 4,
    "OTHERS" : 5
}

#Due to scaling of community pool share, dot was falling below initial liquidity incentive setting, reduce 0.00735 to 0.005 when pool fully established.
Minimums = {
    1 : 0.15,
    9 : 0.03,
    674 : 0.05,
    704 : 0.10,
    712 : 0.10,
    773 : 0.005,
    840 : 0.005
}

Maximums = {
    1 : 0.25,
    549 : 0,
    637 : 0,
    557 : 0.000003985,
    621 : 0.000007405,
    553 : 0.000054405,
    461 : 0.000016185,
    613 : 0.000007365,
    197 : 0.000020515,
    619 : 0.00002427,
    644 : 0.00002285,
    571 : 0.00003265,
    6 : 0.000056385
}

#Causes Maturity to be overruled, use for 1 proposal when changing minimums or matching incentives to ensure they are met
MaturityExceptions = [
    604,
    611,
    549,
    637,
    557,
    621,
    553,
    461,
    613,
    197,
    619,
    644,
    571,
    6 
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

community_pool_share = 0.43
total_incentive_share = 1 - community_pool_share
