# https://leetcode.com/problems/partition-equal-subset-sum/

def brute_force(nums, idx, left_part, right_part, cache):
    """
    brute force: instead of thinking about it as two arrays you have to fill (because you don't need to actually list out the exact array arrangement),
    think of it as two numbers you increment and decrement. you want to visit each number and decide if you want to choose the number and increment / decrement,
    or you move on.

    it's 2^n run time
    """
    # after looking through all the numbers and no combination is viable in this branch
    if idx == len(nums):
        return False

    # if you found right combination
    if left_part == right_part:
        return True

    # if left ends up less than right and you haven't found the right combo, you won't be able to in this sub branch
    if left_part > right_part:
        return False

    # picking
    picking = brute_force(nums, idx + 1, left_part + nums[idx], right_part - nums[idx], cache)
    # not picking
    not_picking = brute_force(nums, idx + 1, left_part, right_part, cache)

    if picking is True or not_picking is True:
        return True

    return False

def bottom_up(nums):
    """
    have a matrix where x axis = half way point (total / 2) and y axis = the elements themselves
    the cell data is True and False. True and False meaning if you chose to put this element in your subset, you'll be able to build
    to the value in Y axis.
    """
    total = sum(nums)
    if total % 2 != 0:
        return False

    # create matrix
    matrix = []
    for _ in range(len(nums) + 1):
        buf = []
        for _ in range((total // 2) + 1):
            buf.append(False)

        matrix.append(buf)

    # mark first column as all true
    for row in matrix:
        row[0] = True

    for y in range(1, len(matrix)):
        num = nums[y - 1]
        for x in range(1, len(matrix[y])):
            unpicked_bool = matrix[y - 1][x]
            if x < num:
                matrix[y][x] = unpicked_bool
            else:
                matrix[y][x] = unpicked_bool or matrix[y - 1][x - num]

    return matrix[-1][-1]
