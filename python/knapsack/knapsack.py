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


# using overlapping subproblem to solve
def _solve_optimized(bag_size, cakes):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (bag_size + 1)

    for capacity in range(bag_size + 1):
        # find the highest possible value you can get for each capacity
        # starting from smallest capacity. larger capacities will use data of
        # possible largest value from smaller capacities. dynamic programming baby
        max_value_for_this_capacity = 0
        for weight, value in cakes:
            # if we found a cake that weighs 0 and value is more than 0,
            # we return infinite, because we can grab an _unlimited_ number
            # of cakes into our bag
            if weight == 0 and value >= 0:
                return float("inf")

            # we don't care about any cakes larger than our current capacity
            if weight > capacity:
                continue

            # If the cake weighs as much or less than the current capacity
            # see what our max value could be if we took it!
            remaining_bag_size_after_taking_cake = capacity - weight
            max_value_using_cake = value + max_values_at_capacities[remaining_bag_size_after_taking_cake]

            max_value_for_this_capacity = max(max_value_for_this_capacity, max_value_using_cake)

        max_values_at_capacities[capacity] = max_value_for_this_capacity

    return max_values_at_capacities[bag_size]
