def max_subarray(nums, k):
    # fixed sliding window problem
    # find max possible summed subarray value of k elements. k is 1 indexed
    max_num = float("-inf")
    current_num = 0
    for idx, num in enumerate(nums):
        current_num += num
        if idx >= k:
            current_num -= nums[idx - k]
            max_num = max(max_num, current_num)

    return max_num
