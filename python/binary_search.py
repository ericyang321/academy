def binary_search(data, val, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if data[mid] == val:
        return mid
    elif data[mid] > val:
       return binary_search(data, val, low, mid - 1)
    else:
        return binary_search(data, val, mid + 1, high)

