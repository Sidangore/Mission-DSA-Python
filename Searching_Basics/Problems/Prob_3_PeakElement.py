def peak_element(nums):
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == high or nums[mid] >= nums[mid + 1]):
            return mid
        elif mid > 0 and nums[mid - 1] >= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == '__main__':
    arrays = [[5, 10, 20, 15], [10, 20, 15, 2, 23, 90, 90], [1, 1, 1]]
    for i in arrays:
        print(i, peak_element(i))


