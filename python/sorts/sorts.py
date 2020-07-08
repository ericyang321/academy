from .comparators import num_comparator
import heapq


def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


def bubble_sort(l):
    pass


def selection_sort(l):
    pass


def insertion_sort(l):
    pass


################# merge sort ##################


def merge_sorted_lists(a_list, b_list, comparator):
    A_LEN = len(a_list)
    B_LEN = len(b_list)

    a_idx = 0
    b_idx = 0

    combined_list = []

    while a_idx < A_LEN and b_idx < B_LEN:
        a_item = a_list[a_idx]
        b_item = b_list[b_idx]

        pre_order_result = comparator(a_item, b_item)
        post_order_result = comparator(b_item, a_item)

        if pre_order_result < post_order_result:
            combined_list.append(a_item)
            a_idx += 1
        else:
            combined_list.append(b_item)
            b_idx += 1

    # concat any other list's left over items when
    # one list has its items exhausted
    if a_idx < A_LEN:
        for idx in range(a_idx, A_LEN):
            combined_list.append(a_list[idx])
    elif b_idx < B_LEN:
        for idx in range(b_idx, B_LEN):
            combined_list.append(b_list[idx])

    return combined_list


def merge_sort(sortable, comparator=num_comparator):
    if len(sortable) <= 1:
        return sortable

    half_idx = len(sortable) // 2
    left_half = sortable[:half_idx]
    right_half = sortable[half_idx:]

    # recurse
    sorted_left_half = merge_sort(left_half, comparator)
    sorted_right_half = merge_sort(right_half, comparator)

    return merge_sorted_lists(sorted_left_half, sorted_right_half, comparator)


################# heap sort ##################


def heap_sort(sortable, comparator=num_comparator):
    sorted_list = []
    heapq.heapify(sortable)

    while len(sortable) > 0:
        item = heapq.heappop(sortable)
        sorted_list.append(item)

    return sorted_list


################# quick sort ##################


def qs_partition_array(sortable, start_idx, end_idx):
    pivot_idx = end_idx
    pivot_val = sortable[pivot_idx]
    left_idx = start_idx
    right_idx = end_idx

    while left_idx <= right_idx:
        # walk left idx pointer to the right until a larger-than-pivot
        # value found
        while left_idx <= right_idx and sortable[left_idx] <= pivot_val:
            left_idx += 1

        # walk right idx pointer to the left until a smaller-than-pivot
        # valud found
        while right_idx >= left_idx and sortable[right_idx] >= pivot_val:
            right_idx -= 1

        # if differences found and the indexes are in the right place, swap them
        if left_idx < right_idx:
            swap(sortable, left_idx, right_idx)
        # unless we've crossed the indexes. then it's time to swap the pivot with the
        # left index and return
        else:
            swap(sortable, left_idx, pivot_idx)

    return left_idx


def quicksort_sublist(sortable, start_idx, end_idx):
    # finished if array has one or less elements
    if start_idx >= end_idx:
        return

    new_pivot = qs_partition_array(sortable, start_idx, end_idx)

    # recurse on smaller parts
    quicksort_sublist(sortable, start_idx, new_pivot - 1)
    quicksort_sublist(sortable, new_pivot + 1, end_idx)


def quicksort(sortable):
    quicksort_sublist(sortable, 0, len(sortable) - 1)
