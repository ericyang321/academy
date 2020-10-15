# 0 / 1 knapsack problem
# you have two arrays [weight, weight] and [value, value]. idx binds weight and value of object
# you have a bag of weight n
# find out what the maximum value of items you can carry in your bag without going over weight


def knapsack(weights, values, bag_size):
    # initialize a matrix where Y axis is the idx of the items
    # and X axis is the incrementing bag sizes
    matrix = []
    for _ in range(len(values) + 1):
        buf = []
        for _ in range(bag_size + 1):
            buf.append(0)

        matrix.append(buf)

    for item_idx in range(1, len(matrix)):
        for size in range(1, len(matrix[item_idx])):
            current_weight = weights[item_idx - 1]
            current_val = values[item_idx - 1]

            # move on if we cannot fit current item into current sack size
            if current_weight > size:
                matrix[item_idx][size] = matrix[item_idx - 1][size]
                continue

            # max value from choosing not to take current item
            skip_max_val = matrix[item_idx - 1][size]

            # max value from choosing to take current item
            prev_take_max_val = 0
            prev_take_max_val_idx = size - current_weight
            if prev_take_max_val_idx >= 0:
                prev_take_max_val = (matrix[item_idx - 1][prev_take_max_val_idx]) + current_val

            matrix[item_idx][size] = max(skip_max_val, prev_take_max_val)

    return matrix[-1][-1]


print(
    knapsack(weights=[3, 1, 3, 4, 2], values=[2, 2, 4, 5, 3], bag_size=7)
)
