

incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 22, 42,
    183, 197,
    461, 463, 464, 481, 482, 497, 498,
    548, 549, 553, 557, 571, 573, 574, 577, 584, 585, 586,
    600, 601, 602, 604, 605, 608, 611, 613, 619, 621, 625, 626, 627, 629, 637, 641, 644, 648, 651, 674, 678, 681, 690,
    704, 712, 722
    ]

#577 XKI, Ends 13th August 2022
#600 and 601 CMDX, Ends 10th September 2022
#604 and 611 STARS, Ends 7th October 2022
#648 PSTAKE, Ends 5th August 2022
#690 MNTL, Ends 16th September 2022
#15 and #715, XPRT, Ends 22nd August

matched_pool_ids = [
    577,
    600, 601, 
    604, 611,
    648, 
    690,
    15, 719
    ]

Majors = ["ATOM", "CRO", "WETH", "WBTC"]

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

Minimums = {
    1 : 0.15,
    9 : 0.03,
    674 : 0.05,
    704 : 0.10,
    712 : 0.10
}

Maximums = {
    1 : 0.25,
    548 : 0,
    8 : 0,
    574 : 0,
    22 : 0,
    464 : 0,
    183 : 0
}

#Causes Maturity to be ignored, use for 1 proposal only when changing minimums to ensure they are met
MaturityExceptions = [
    548,
    8,
    574,
    22,
    464,
    183,
    15,
    719
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
