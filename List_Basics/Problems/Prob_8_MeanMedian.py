import math


def median(arr, n):
    arr.sort()

    if n % 2 != 0:
        return arr[n // 2]
    return math.floor((arr[n // 2] + arr[(n // 2) - 1]) / 2)


def mean(arr, n):
    return sum(arr) // n


if __name__ == '__main__':
    nums = list(map(int, input("Enter nums: ").strip().split()))
    n = len(nums)
    print(mean(nums, n), median(nums, n))

