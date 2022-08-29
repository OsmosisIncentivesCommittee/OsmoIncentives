incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 15, 42,
    197,
    461, 463, 481, 482, 497, 498,
    549, 553, 557, 571, 573, 577, 584, 585, 586,
    600, 601, 602, 604, 605, 608, 611, 613, 619, 621, 625, 626, 627, 629, 637, 641, 644, 648, 651, 674, 678, 681, 690,
    704, 712, 722, 725, 730, 731, 773
    ]

#604 and 611 STARS, Ends 7th October 2022
#690 MNTL, Ends 16th September 2022
#722, EVMOS, ends 18th October 2022

matched_pool_ids = [
    604, 611,
    690,
    722
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC", "DOT"]

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
    773 : 0.00735
}

Maximums = {
    1 : 0.25,
    600: 0,
    601: 0
}

#Causes Maturity to be overruled, use for 1 proposal when changing minimums or matching incentives to ensure they are met
MaturityExceptions = [
    600, 601, 725
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

community_pool_share = 0.29
total_incentive_share = 1 - community_pool_share
