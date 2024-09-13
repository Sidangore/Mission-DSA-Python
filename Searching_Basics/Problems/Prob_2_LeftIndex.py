def left_index(nums, x):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if x > nums[mid]:
            low = mid + 1
        elif x < nums[mid]:
            high = mid - 1
        else:
            if nums[mid] == x and (mid == 0 or nums[mid - 1] != nums[mid]):
                return mid
            else:
                high = mid - 1

    return - 1


if __name__ == '__main__':
    arrays = [[1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10],
              [7, 7, 14, 21, 28, 28, 35, 42, 49, 49, 56, 63, 70],
              [10, 10, 20, 30, 30, 40, 50, 60, 70, 70, 80, 90, 100, 100],
              [3, 3, 6, 9, 12, 12, 15, 18, 18, 21, 24, 27, 27, 30],
              [100, 100, 200, 300, 300, 400, 500, 500, 600, 700, 800, 900, 1000, 1000]]
    xs = [5, 49, 30, 24, 301]

    for i in range(len(xs)):
        print(arrays[i], xs[i], left_index(arrays[i], xs[i]))
