def array_partition_1(numbers):
    """
    sorting: O(n log n)
    adding it all up: O(n)

    O(2n log n)
    """
    sorted_numbers = sorted(numbers)
    max_num = 0
    i = 0
    while i < len(sorted_numbers):
        max_num += sorted_numbers[i]
        i += 2

    return max_num
