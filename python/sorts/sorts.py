def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp


def bubble_sort(l):
    """
    NOT IMPORTANT TO KNOW. bubble sort is really fucking bad
    O(n^2)
    http://books.cs.luc.edu/introcs-csharp/arrays/sorting.html#bubble-sort
    """
    llen = len(l)
    for i in range(llen - 1, -1, -1):
        for j in range(0, i):
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)


def selection_sort(l):
    """
    O(n^2)
    http://books.cs.luc.edu/introcs-csharp/arrays/sorting.html#selection-sort
    """
    for i in range(0, len(l) - 1):
        min_int = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_int]:
                min_int = j

        if min_int != i:
            swap(l, min_int, i)


def insertion_sort(l):
    """
    O(n^2)
    http://books.cs.luc.edu/introcs-csharp/arrays/sorting.html#insertion-sort
    """
    pass
