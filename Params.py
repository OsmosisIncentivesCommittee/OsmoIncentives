

incentivized_pool_ids = [
    1,2,3,4,5,6,7,8,9,10,13,15,22,42,
    151,183,197,461,463,464,481,482,497,547,548,
    553,555,557,558,560,561,562,565,567,571,572,573,574,577,578,584,585,586,587,596,597,600,
    601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,
    651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,
    701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743
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
    1 : 0.25
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

community_pool_share = 0.29
total_incentive_share = 1 - community_pool_share
