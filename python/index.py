# you steal cakes. you broke into a cake vault
# there are unlimited supply of cakes in there but only a limited type of cakes
# cakes are represented as

# tuple of ints (0, 1), where 0 is weight of cake (kilos) and 1 is the monetary value of cake (shilling)

# you brought a duffle. it can only carry x amount of weight.
# you want to make off with the most amount of money by stealing cake

# write a func that takes a list of cake tuples and a duffle weight capacity,
# and return the maximum monetary value one can steal with duffle.
#

# example: max_duffle_bag_value(30, [(7, 160), (3, 90), (2, 15)])

# brute force

# def find_viable_combo_cakes(duffle_weight, cakes):
#     # base case: we've over reached and the duffle can't carry this much
#     if duffle_weight <= 0:
#         return 0
#     # base case: we overreached on cakes idx
#     if cakes is None or len(cakes) == 0:
#         return 0

#     # func: find every possible cake type multiple combination that fits in a duffle

# def brute_max_duffle_bag_value(duffle_weight, cakes):
#     combos = find_viable_combo_cakes()

#     most_steal = 0
#     for combo in combos:
#         score = 0
#         for cake in combo:
#             score += cake[1]

#         if score > most_steal:
#             most_steal = score

#     return most_steal


# print(brute_max_duffle_bag_value(30, [(7, 160), (3, 90), (2, 15)]))
