# knapsack problem

# You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.

# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

# Each type of cake has a weight and a value, stored in a tuple with two indices:

# 1. An integer representing the weight of the cake in kilograms
# 2. An integer representing the monetary value of the cake in British shillings

# For example:
# Weighs 7 kilograms and has a value of 160 shillings
# (7, 160)

# Weighs 3 kilograms and has a value of 90 shillings
# (3, 90)

# You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.

# For example:
# cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
# max_duffel_bag_value(cake_tuples, capacity)

# Weights and values may be any non-negative integer. Yes, it's weird to think about cakes that weigh nothing or duffel bags that can't hold anything. But we're not just super mastermind criminals—we're also meticulous about keeping our algorithms flexible and comprehensive.


def max_cake_money(bag_size, cakes):
    # return _solve_brute(bag_size, cakes, 0, 0)
    # return _solve_cache(bag_size, cakes, 0, 0, {})
    return _solve_optimized(bag_size, cakes)


def _solve_brute(bag_size, cakes, current_monetary_value, idx):
    # found a perfectly filled bag
    if bag_size == 0:
        return current_monetary_value
    # bag is too large
    if bag_size < 0:
        return -1

    weights = []
    for i in range(idx, len(cakes)):
        cake_weight, monetary_value = cakes[i]

        maxed_cake_value = _solve_brute(
            bag_size - cake_weight, cakes, current_monetary_value + monetary_value, i
        )
        if maxed_cake_value == -1:
            weights.append(current_monetary_value)
        else:
            weights.append(maxed_cake_value)

    return max(weights)


def _solve_cache(bag_size, cakes, current_monetary_value, idx, cache):
    # found a perfectly filled bag
    if bag_size == 0:
        return current_monetary_value
    # bag is too large
    if bag_size < 0:
        return -1

    weights = []
    for i in range(idx, len(cakes)):
        cake_weight, monetary_value = cakes[i]

        cache_key = str(
            [bag_size - cake_weight, current_monetary_value + monetary_value]
        )

        if cache_key in cache:
            maxed_cake_value = cache[cache_key]
        else:
            maxed_cake_value = _solve_cache(
                bag_size - cake_weight,
                cakes,
                current_monetary_value + monetary_value,
                i,
                cache,
            )
            cache[cache_key] = maxed_cake_value

        if maxed_cake_value == -1:
            weights.append(current_monetary_value)
        else:
            weights.append(maxed_cake_value)

    return max(weights)


def _solve_optimized(bag_size, cakes):
    # you have cakes of weights 1 -> infinite

    # imagine if you had a bag size of only 1
    # for something this small, we only care to look at cakes the weight of 1
    # and we would iterate through all cakes and save the maximum value of a cake that has a weight of 1.

    # imagine then, you had a bag size of 2
    # if we pick a cake of weight 2, we would fill up our entire bag.
    # we just need to check if picking a cake size of 2 would be better money than if we picked
    # another cake of weight 1.
    # but we have to account for cakes the weight of 1.
    # we could pick up a cake weight 1, but we would still have more space in the bag.
    # the best way to fill up that extra space is to check if adding another cake of weight 1 has a higher price
    # than the current max price of filling up a cake size 2.
    None


# _solve_optimized(3, [(1, 1), (2, 2), (3, 3)])
