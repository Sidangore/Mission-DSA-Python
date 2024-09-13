def last_occ_itr(nums, x):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if x < nums[mid]:
            high = mid - 1
        elif x > nums[mid]:
            low = mid + 1
        else:
            if mid == high or nums[mid] != nums[mid + 1]:
                return mid
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    arrays = [[10, 20, 30, 40, 50, 60, 70], [1, 10, 10, 10, 20, 20, 40], [10, 20, 30], [15, 15, 15], [10, 15, 20, 20, 40, 40, 50], [5, 8, 8, 10, 10], [8, 10, 10, 12]]
    xs = [20, 20, 15, 15, 20, 10, 7]
    for i in range(len(xs)):
        print(arrays[i], xs[i], last_occ_itr(arrays[i], xs[i]))
