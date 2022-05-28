

incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 22, 42, 183, 197, 461, 463, 464, 481, 482, 497, 498,
    548, 553, 555, 557, 558, 571, 572, 573, 574, 577, 584,
    585, 586, 587, 596, 597, 600, 601, 602, 604, 605, 606, 608, 611, 613, 616,
    617, 618, 619, 621, 625, 626, 627, 629, 631, 637, 638, 641, 643, 644, 645, 648, 649, 651, 662, 674, 678, 681, 690, 704, 712
    ]

matched_pool_ids = [
    3, 497, 498, 553, 555, 560, 562, 571, 572, 573, 574, 577, 578, 592, 600, 601, 604, 605, 606,
    611, 612, 618, 619, 637, 638, 641, 643, 648, 651, 719
    ]

Majors = ["ATOM", "CRO", "axlWETH", "axlWBTC"]

Stables = ["EEUR", "axlUSDC", "axlDAI"]

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
    1 : 0.25,
    712 : 0.05,
    704 : 0.05,
    674 : 0.05
}


match_limit = 0.30
adjust_scale = 0.25
entry_window = 4

swap_fee_cap = 3
match_multiple_cap = 1

share_1 = 0.5
share_7 = 0.3
share_14 = 0.2

gauge_precision = 100000000

community_pool_share = 0.20
total_incentive_share = 1 - community_pool_share
