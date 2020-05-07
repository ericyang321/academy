def highest_products_with_space(nums, num_to_multiply=3):
    """
    conditions of highest products
    - 3 highest positive integers
    - 1 highest positive integers, 2 lowest negative integer
    - no 0s

    find a list of the 3 highest positive integers
    find a list of 2 of the lowest negative integers

    compare between (3 highest positive integers multipled) and (2 lowest negative integers multipled * highest positive integer)
    and choose one

    test cases
    [1, 1, 1, 1, 1, 4, 5] # 1 4 5 -> 20
    [-1, -2, -3, -4, 1, 2, 3] # -3, -4, 3 -> 36

    1. iterate through nums
    2. find 3 highest ints, push them into buf
    3. find 2 lowest negative ints, push them into buf
    """

    if nums == []:
        return 0

    if len(nums) < 3:
        raise ValueError("There needs to be more than 3 numbers to multiply")

    highest_nums_idx = []
    lowest_negative_nums_idx = []

    # number of negative numbers to multiply that will result in a positive number
    num_of_negative_nums = num_to_multiply if num_to_multiply % 2 == 0 else (num_to_multiply - 1)

    for _ in range(0, num_to_multiply):
        high_idx = find_highest_idx_excluding(nums, highest_nums_idx)
        highest_nums_idx.append(high_idx)

    for _ in range(0, num_of_negative_nums):
        low_idx = find_lowest_idx_excluding(
            nums, lowest_negative_nums_idx + highest_nums_idx
        )
        if low_idx is None:
            continue

        lowest_negative_nums_idx.append(low_idx)

    highest_nums = [nums[idx] for idx in highest_nums_idx]
    lowest_nums_with_highest_combined = [
        nums[idx] for idx in lowest_negative_nums_idx
    ] + [max(highest_nums)]

    highest_nums_combined = multiply(highest_nums)
    lowest_nums_with_highest_combined = multiply(lowest_nums_with_highest_combined)

    return (
        highest_nums_combined
        if highest_nums_combined >= lowest_nums_with_highest_combined
        else lowest_nums_with_highest_combined
    )


def find_highest_idx_excluding(nums, excluded_idxs):
    highest_idx = None

    for idx in range(0, len(nums)):
        if idx not in excluded_idxs:
            highest_idx = idx
            break

    if highest_idx is None:
        return None

    for idx, num in enumerate(nums):
        if idx in excluded_idxs:
            continue

        if num > nums[highest_idx]:
            highest_idx = idx

    return highest_idx


def find_lowest_idx_excluding(nums, excluded_idxs):
    lowest_idx = None

    for idx in range(0, len(nums)):
        if nums[idx] < 0 and idx not in excluded_idxs:
            lowest_idx = idx
            break

    if lowest_idx is None:
        return None

    for idx, num in enumerate(nums):
        if idx in excluded_idxs or num > 0:
            continue

        if num < nums[lowest_idx]:
            lowest_idx = idx

    return lowest_idx


def multiply(nums):
    prod = 1
    for num in nums:
        prod *= num

    return prod
