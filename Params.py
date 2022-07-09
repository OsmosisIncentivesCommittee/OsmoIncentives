

incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 22, 42,
    183, 197,
    461, 463, 464, 481, 482, 497, 498,
    548, 549, 553, 555, 557, 558, 571, 572, 573, 574, 577, 584, 585, 586, 587, 596, 597,
    600, 601, 602, 604, 605, 606, 608, 611, 613, 616, 617, 618, 619, 621, 625, 626, 627, 629, 631, 637, 638, 641, 643, 644, 645, 648, 649, 651, 662, 674, 678, 681, 690,
    704, 712, 722
    ]

matched_pool_ids = [
    3,
    573, 574, 
    577,
    600, 601, 
    604, 611,
    605, 606, 
    618, 619, 
    637, 
    648, 651, 690,
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
    587 : 0,
    572 : 0,
    606 : 0,
    643 : 0,
    618 : 0,
    555 : 0,
    645 : 0,
    558 : 0,
    617 : 0,
    616 : 0,
    638 : 0,
    597 : 0,
    596 : 0,
    649 : 0,
    631 : 0,
    662 : 0
}

#Causes Maturity to be ignored, use for 1 proposal only when changing minimums to ensure they are met
MaturityExceptions = [
    587,
    572,
    606,
    643,
    618,
    555,
    645,
    558,
    617,
    616,
    638,
    597,
    596,
    649,
    631,
    662,
    690
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
