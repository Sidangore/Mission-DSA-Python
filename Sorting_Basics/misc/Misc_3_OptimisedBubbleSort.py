from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            return


if __name__ == '__main__':
    nums = [24, 12, 17, 52, 48, 24]
    bubble_sort(nums)
    print(nums) # [12, 17, 24, 24, 48, 52]
