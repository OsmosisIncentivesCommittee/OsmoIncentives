

incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 22, 42,
    183, 197,
    461, 463, 464, 481, 482, 497, 498,
    548, 549, 553, 557, 571, 573, 574, 577, 584, 585, 586,
    600, 601, 602, 604, 605, 608, 611, 613, 619, 621, 625, 626, 627, 629, 637, 641, 644, 648, 651, 674, 678, 681, 690,
    704, 712, 722
    ]

matched_pool_ids = [
    3,
    497, 498,
    553, 555, 571, 572, 573, 574, 577,
    600, 601, 604, 605, 606, 611, 618, 619, 637, 638, 641, 643, 648, 651, 690,
    719
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC"]

Stables = ["EEUR", "USDC", "DAI"]

Category_weights = {
    "OSMO_MAJOR" : 0.45,
    "OSMO_STABLE" : 0.30,
    "OSMO_MINOR" : 0.20,
    "MAJOR_STABLE" : 0,
    "STABLESWAP" : 0,
    "OTHERS" : 0.05
}

Category_Order = {
    "OSMO_STABLE" : 0,
    "OSMO_MAJOR" : 1,
    "MAJOR_STABLE" : 2,
    "STABLESWAP" : 3,
    "OSMO_MINOR" : 4,
    "OTHERS" : 5
}

Minimums = {
    1 : 0.15,
    9 : 0.03,
    674 : 0.05,
    704 : 0.10,
    712 : 0.10
}

Maximums = {
    1 : 0.25,
}

#Causes Maturity to be ignored, use for 1 proposal only when changing minimums to ensure they are met
MaturityExceptions = [
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

community_pool_share = 0.20
total_incentive_share = 1 - community_pool_share
