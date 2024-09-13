def floor_arr(nums, x):
    n = len(nums)
    low, high = 0, n - 1

    if x < nums[low]:
        return -1
    elif x > nums[high]:
        return high

    while low <= high:
        mid = low + (high - low) // 2

        if x == nums[mid]:
            return mid
        elif mid > 0 and nums[mid - 1] < x < nums[mid]:
            return mid - 1
        elif x > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    arrs = [[1, 2, 8, 10, 11, 12, 19], [1, 2, 8, 10, 11, 12, 19], []]
    xs = [0, 5]
    for i in range(len(xs)):
        print(floor_arr(arrs[i], xs[i]))
