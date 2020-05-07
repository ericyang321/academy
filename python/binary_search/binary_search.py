def binary_search(nums, target):
    floor_idx = 0
    ceil_idx = len(nums) - 1

    while floor_idx <= ceil_idx:
        diff = int((ceil_idx - floor_idx) / 2)
        half_distance_val = nums[floor_idx + diff]

        if half_distance_val == target:
            return True

        if target < half_distance_val:
            ceil_idx = half_distance_val - 1
        else:
            floor_idx = half_distance_val + 1

    return False
