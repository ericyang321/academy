def jewels_and_stones(J, S):
    """
    https://leetcode.com/problems/jewels-and-stones/
    """
    count = 0
    chars = [char for char in J]
    gem_list = set(chars)

    for stone in S:
        if stone in gem_list:
            count += 1

    return count
