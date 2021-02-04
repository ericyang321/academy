def min_subarray(nums, k):
    # dynamic sliding window problem
    # find smallest subarray with summed value greater than or equal to k
    # smallest subarray means the smallest len of subarray capable of summing greater than or equal to k

    # as the window slides, if a sum is found to be greater than 8, slide the left end of window to the right to shrink the subarray
    # if a sum is found to be smaller than 8, slide the right end of window and increase window size to get a larger number

    smallest_subarray_size = len(nums)
    current_sum = 0
    start_idx = 0
    for end_idx in range(0, len(nums)):
        current_sum += nums[end_idx]
        while current_sum >= k:
            smallest_subarray_size = min(
                smallest_subarray_size, end_idx - start_idx + 1
            )
            current_sum -= nums[start_idx]
            start_idx += 1

    if current_sum < 8:
        return -1

    return smallest_subarray_size
