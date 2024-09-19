def hoares(nums, low, high):
    pivot = nums[low]
    i = low - 1
    j = high + 1

    while True:
        i = i + 1
        while nums[i] < pivot:
            i = i + 1

        j = j + 1
        while nums[j] > pivot:
            j = j + 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]
    