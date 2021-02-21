def ways_to_group(k, n):
    """
    a permutation problem
    given n things, how many different ways are there to choose k of them?
    given 8 people, how many ways are there to group 3 of them to go to the movies? (without repeating)

    pretend you're just choosing a person. if that person is in the group, then we need to find C(k - 1, n - 1).
    if that person is NOT in the group, we need to find C(k, n - 1)

    the sub problem is to minus from k and n to create decrementing persons scenarios until you get to a viable possibility:
    1. k == 0. There's no more space left in the group. you found a combo.
    2. n == k. Possiblity where you've choosen to not choose _anyone_ in your group except for the last k here that you have to take. this is an end combo

    otherwise you want to keep exploring possibilities through `C(k - 1, n - 1)` + `c(k, n - 1)`
    """

    # found a viable grouping
    if k == 0 or k == n:
        return 1

    if k > n:
        return 0

    return ways_to_group(k, n - 1) + ways_to_group(k - 1, n - 1)
