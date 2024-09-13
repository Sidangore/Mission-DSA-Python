def first_occ_rec(nums, x, low, high):
    if low <= high:
        mid = (low + high) // 2
        if nums[mid] < x:
            return first_occ_rec(nums, x, mid + 1, high)
        elif nums[mid] > x:
            return first_occ_rec(nums, x, low, mid - 1)
        else:
            if mid == 0 or nums[mid - 1] != nums[mid]:
                return mid
            else:
                return first_occ_rec(nums, x, low, mid - 1)

    return -1


if __name__ == '__main__':
    arrays = [[10, 20, 30, 40, 50, 60, 70], [1, 10, 10, 10, 20, 20, 40], [10, 20, 30], [15, 15, 15]]
    xs = [20, 20, 15, 15]
    for i in range(len(xs)):
        print(first_occ_rec(arrays[i], xs[i], 0, len(arrays[i]) - 1))
