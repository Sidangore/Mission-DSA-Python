def last_occ_rec(nums, x, low, high):
    if low <= high:
        mid = (low + high) // 2
        if x < nums[mid]:
            return last_occ_rec(nums, x, low, mid - 1)
        elif x > nums[mid]:
            return last_occ_rec(nums, x, mid + 1, high)
        else:
            if mid == high or nums[mid] != nums[mid + 1]:
                return mid
            else:
                return last_occ_rec(nums, x, mid + 1, high)

    return -1


if __name__ == '__main__':
    arrays = [[10, 20, 30, 40, 50, 60, 70], [1, 10, 10, 10, 20, 20, 40], [10, 20, 30], [15, 15, 15],
              [10, 15, 20, 20, 40, 40, 50], [5, 8, 8, 10, 10], [8, 10, 10, 12], [10, 10, 10, 10, 10, 10]]
    xs = [20, 20, 15, 15, 20, 10, 7, 10]
    for i in range(len(xs)):
        print(arrays[i], xs[i], last_occ_rec(arrays[i], xs[i], 0, len(arrays[i]) - 1))
