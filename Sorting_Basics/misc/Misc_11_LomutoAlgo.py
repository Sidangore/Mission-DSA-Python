def lomuto(nums, low, high):
    p = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < p:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[high], nums[i + 1] = nums[i + 1], nums[high]
    return i + 1
