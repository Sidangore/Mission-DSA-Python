def count1s(nums):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == 1 and (mid == high or nums[mid + 1] == 0):
            return mid + 1
        if nums[mid] == 0:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == '__main__':
    arrays = [[1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]
    for arr in arrays:
        print(arr, count1s(arr))
