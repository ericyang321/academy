# recursively find the possible permutation combinations of a unique string's characters

def recursive_get_all_permutations(string):
    # base case. when theres only one, just return the set with one char in it
    if len(string) <= 1:
        return set([string])

    except_last = string[:-1]
    last = string[-1]

    # recursive call. get all possible permutations of characters except the last one
    permutations_except_last = recursive_get_all_permutations(except_last)

    permutations = set()
    for permutation in permutations_except_last:
        # len(arr) + 1 because [:] notation is non-inclusive.
        # the + 1 is there to make sure you get the position _after_ the last item in the array
        # since our [:] notation is positioned _after_ a character, not before
        for insert_position in range(0, len(permutations_except_last) + 1):
            pre = permutation[:insert_position]
            post = permutation[insert_position:]

            print(pre + last + post)

            permutations.add(pre + last + post)

    return permutations
