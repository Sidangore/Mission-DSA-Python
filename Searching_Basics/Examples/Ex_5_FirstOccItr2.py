def first_occ_itr(nums, x):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if x < nums[mid]:
            high = mid - 1
        elif nums[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] != nums[mid]:
                return mid
            else:
                high = mid - 1

    return -1


if __name__ == '__main__':
    arrays = [[10, 8, 30, 4, 5], [10, 20, 30, 40, 50, 60, 70], [1, 10, 10, 10, 20, 20, 40], [10, 20, 30], [15, 15, 15]]
    xs = [5, 20, 20, 15, 15]
    for i in range(len(xs)):
        print(first_occ_itr(arrays[i], xs[i]))
