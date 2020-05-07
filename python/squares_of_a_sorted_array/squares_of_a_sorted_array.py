def squares_of_a_sorted_array(array):
    """
    https://leetcode.com/problems/squares-of-a-sorted-array/
    """
    return optimized_solution(array)


def brute_force(array):
    """
    n log(n) * o(n)
    """
    squared_ints = [x * x for x in array]
    return sorted(squared_ints, reverse=True)


def optimized_solution(array):
    """
    O(5n)
    sectionizing + reverse + square + square + merge
    """
    negatives, positives = sectionize_arrays(array)
    return merge_two_sorted_arrays(reversed(square(negatives)), square(positives))


def sectionize_arrays(array):
    for i, num in enumerate(array):
        if num > 0:
            return (array[0:i], array[i:])

    return (array, [])


def merge_two_sorted_arrays(array1, array2):
    merged = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(array1) and pointer2 < len(array2):
        num1 = array1[pointer1]
        num2 = array2[pointer2]
        if num1 <= num2:
            merged.append(num1)
            pointer1 += 1
        else:
            merged.append(num2)
            pointer2 += 1

    # merge remaining leftover items in array 1
    while pointer1 < len(array1):
        merged.append(array1[pointer1])
        pointer1 += 1

    # merge remaining leftover items in array 2
    while pointer2 < len(array2):
        merged.append(array2[pointer2])
        pointer2 += 1

    return merged


def square(array):
    return [x * x for x in array]
