# given a dollar amount and a list of coin denominations [1, 2, 3], find the possible ways to combine denominations to get to dollar amount
# (4, [1, 2, 3]) returns 4
# 4 as in [1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]

# http://www.pythontutor.com/visualize.html#mode=edit

# the three possible patterns of solving a recursive problem
# 1. the naive terrible recursive way:
def coins_recursive(amount, denominations, current_index=0):

    # func: find combinations of coins that will total to amount
    # we need to break this down to sub problem.
    # sub problem is: how many ways to get remaining amount from remaining denominations
        # aka how many ways to get smaller amount from a smaller segment of denominations


    # 0 means we found a viable combination
    if amount == 0:
        return 1
    # < 0 means we did not find a viable combination
    elif amount < 0:
        return 0
    # no more denominations
    elif current_index == len(denominations):
        return 0

    print(
        "checking ways to make {} with {}".format(
            amount, denominations[current_index:],
        )
    )

    current_coin = denominations[current_index]

    combinations_count = 0
    while amount >= 0:
        combinations_count += coins_recursive(amount, denominations, current_index + 1)

        amount -= current_coin

    return combinations_count


# 2: recursion, but with caching of calculations we've done already
# we should cache at checking for "checking ways to make amount with denominations"
# thats right before the checker dives into a separate tree of possibilities. cut
# that off with a result early with caching
class CachedCoin(object):
    def __init__(self):
        self.cache = {}

    def possibilities(self, amount, denominations, current_index=0):
        cache_key = str((amount, current_index))
        if cache_key in self.cache:
            print("cache hit: {}".format(cache_key))
            return self.cache[cache_key]

        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if current_index == len(denominations):
            return 0

        print(
            "checking ways to make {} with {}".format(
                amount, denominations[current_index:],
            )
        )

        current_coin = denominations[current_index]

        combinations_count = 0
        while amount >= 0:
            combinations_count += self.possibilities(
                amount, denominations, current_index + 1
            )

            amount -= current_coin

        # cache result once computed:
        self.cache[cache_key] = combinations_count
        return combinations_count


# 3: iterative, bottoms up approach that saves space and time but might not be available to all problems
def coins_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[
                higher_amount_remainder
            ]

    return ways_of_doing_n_cents[amount]
