def search_bin(nums, x):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == x:
            return mid
        elif x < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == '__main__':
    inputs = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],
              [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
              [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
              [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]]
    xs = [5, 45, 90, 27, 301]

    for i in range(len(xs)):
        print(inputs[i], xs[i], ": ", search_bin(inputs[i], xs[i]))

