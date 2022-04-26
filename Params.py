

incentivized_pool_ids = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 22, 42, 183, 197, 461, 463, 464, 481, 482, 497, 498,
    548, 553, 555, 557, 558, 560, 561, 562, 565, 567, 571, 572, 573, 574, 577, 578, 580, 584,
    585, 586, 587, 592, 596, 597, 600, 601, 602, 604, 605, 606, 608, 610, 611, 612, 613, 615, 616,
    617, 618, 619, 621, 625, 626, 627, 629, 631, 637, 638, 641, 642, 643, 644, 645, 648, 649, 651, 662
    ]

matched_pool_ids = [
    497, 498, 553, 555, 560, 562, 571, 572, 573, 574, 577, 578, 592, 600, 601, 604, 605, 606,
    611, 612, 618, 619, 637, 638, 641, 643, 648, 651
    ]

Majors = ["ATOM", "LUNA", "CRO"]

Stables = ["UST", "EEUR"]

Category_weights = {
    "OSMO_MAJOR" : 0.40,
    "OSMO_STABLE" : 0.30,
    "OSMO_MINOR" : 0.20,
    "MAJOR_STABLE" : 0.05,
    "STABLESWAP" : 0.001,
    "OTHERS" : 0.0499
}




match_limit = 0.30
adjust_scale = 0.25
entry_window = 4
swap_fee_cap = 3

share_1 = 0.5
share_7 = 0.3
share_14 = 0.2

gauge_precision = 100000000

community_pool_share = 0.01
total_incentive_share = 1 - community_pool_share
