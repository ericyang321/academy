# 0 / 1 knapsack problem
# you have two arrays [weight, weight] and [value, value]. idx is item id or item idx
# find out what the maximum value of items you can carry in your bag without going over weight

from matrix_printer.matrix_printer import print_matrix


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
            # idx - 1 here because item_idx and size are 1 indexed. we need 0 to indicate
            # not taking any items
            current_weight = weights[item_idx - 1]
            current_val = values[item_idx - 1]

            # if we can't fit current item's weight in bag size `size`, copy max value
            # from last item
            if current_weight > size:
                matrix[item_idx][size] = matrix[item_idx - 1][size]
                continue

            # find out the max value of bag if you DON'T take current item
            # and find out max value of your bag if you DO take current item

            # max value from choosing not to take current item
            skip_max_val = matrix[item_idx - 1][size]

            # max value from choosing to take current item
            prev_take_max_val = 0
            # prev value needs to fit. find max value of size - current_weight idx item.
            prev_take_max_val_idx = size - current_weight
            if prev_take_max_val_idx >= 0:
                prev_take_max_val = (
                    matrix[item_idx - 1][prev_take_max_val_idx]
                ) + current_val

            matrix[item_idx][size] = max(skip_max_val, prev_take_max_val)

    return matrix[-1][-1]


# knapsack(weights=[3, 1, 3, 4, 2], values=[2, 2, 4, 5, 3], bag_size=7)
