def count_occ(nums, x):
    f = first_occ(nums, x)
    return 0 if f == -1 else last_occ(nums, x) - f + 1


def first_occ(nums, x):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if x < nums[mid]:
            high = mid - 1
        elif x > nums[mid]:
            low = mid + 1
        else:
            if x == nums[mid] and (mid == 0 or nums[mid - 1] != nums[mid]):
                return mid
            else:
                high = mid - 1

    return -1


def last_occ(nums, x):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if x < nums[mid]:
            high = mid - 1
        elif x > nums[mid]:
            low = mid + 1
        else:
            if x == nums[mid] and (mid == high or nums[mid] != nums[mid + 1]):
                return mid
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    arrays = [[10, 20, 30, 40, 50, 60, 70], [1, 10, 10, 10, 20, 20, 40], [10, 20, 30], [15, 15, 15],
              [10, 15, 20, 20, 40, 40, 50], [5, 8, 8, 10, 10], [8, 10, 10, 12], [10, 10, 10, 10, 10, 10]]
    xs = [20, 20, 15, 15, 20, 10, 7, 10]
    for i in range(len(xs)):
        print(arrays[i], xs[i], count_occ(arrays[i], xs[i]))
