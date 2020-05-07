# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

# For example, given:
#   [1, 7, 3, 4]

# your function would return:
#   [84, 12, 28, 21]

# Here's the catch: You can't use division in your solution!


def get_products_of_all_ints_except_at_index(nums):
    forwards = [1]
    backwards = [1]

    forwards_accu = 1
    for idx in range(0, len(nums) - 1):
        forwards_accu *= nums[idx]
        forwards.append(forwards_accu)

    backwards_accu = 1
    for idx in range(len(nums) - 1, 0, -1):
        backwards_accu *= nums[idx]
        backwards.append(backwards_accu)

    forwards_idx = 0
    backwards_idx = len(nums) - 1

    multiplied = []
    while forwards_idx < len(nums) and backwards_idx >= 0:
        multiplied.append(forwards[forwards_idx] * backwards[backwards_idx])
        forwards_idx += 1
        backwards_idx -= 1

    return multiplied

