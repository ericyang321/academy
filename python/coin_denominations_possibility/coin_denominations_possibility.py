# Your quirky boss collects rare, old coins...
#
# They found out you're a programmer and asked you to solve something they've been wondering for a long time.
#
# Write a function that, given:
#
# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.
#
# for example: (4, [1, 2, 3, 4])
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢


def solve(amount, denominations):
    # return _solve_brute(amount, denominations, 0)
    return _solve_cache(amount, denominations, 0, {})


def _solve_brute(amount, denominations, idx):
    # base case: overshot
    if amount < 0:
        return 0
    # base case: found the correct answer
    if amount == 0:
        return 1

    accumulator = 0
    for i in range(idx, len(denominations)):
        deno = denominations[i]

        accumulator += _solve_brute(amount - deno, denominations, i)

    return accumulator


def _solve_cache(amount, denominations, idx, cache):
    # base case: overshot
    if amount < 0:
        return 0
    # base case: found the correct answer
    if amount == 0:
        return 1

    accumulator = 0
    for i in range(idx, len(denominations)):
        deno = denominations[i]

        key = str((amount, i))

        if key in cache:
            accumulator += cache[key]
        else:
            perm = _solve_cache(amount - deno, denominations, i, cache)
            accumulator += perm
            cache[key] = perm

    return accumulator


print(solve(900, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
