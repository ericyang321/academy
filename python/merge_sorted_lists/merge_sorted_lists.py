def merge_sorted_lists(sorted_list_one, sorted_list_two):
    """
    We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

    For example:

    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    print(merge_lists(my_list, alices_list))

    1. create two index counters, both beginning at list1 0 and list2 0
    2. have them both advance. switch over to the other any time there's a larger one
    3. merge whichever list is empty left (in the case of uneven lists) into the final list
    """

    out = []

    one_p = 0
    two_p = 0

    while one_p < len(sorted_list_one) and two_p < len(sorted_list_two):
        if sorted_list_one[one_p] < sorted_list_two[two_p]:
            out.append(sorted_list_one[one_p])
            one_p += 1
        else:
            out.append(sorted_list_two[two_p])
            two_p += 1

    if one_p < len(sorted_list_one):
        out = out + sorted_list_one[one_p:]
    elif two_p < len(sorted_list_two):
        out = out + sorted_list_two[two_p:]

    return out
