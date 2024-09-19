from typing import List


def insertion_sort(nums: List[int]):
    n = len(nums)

    for i in range(1, n):
        x = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > x:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = x


if __name__ == '__main__':
    nums = [34, 17, 62, 45, 13, 26]
    insertion_sort(nums)
    print(nums)  # [13, 17, 26, 34, 45, 62]