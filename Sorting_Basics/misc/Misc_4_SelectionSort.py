from typing import List


def selection_sort(nums: List[int]):
    n = len(nums)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    nums = [34, 17, 62, 45, 13, 26]
    selection_sort(nums)
    print(nums)  # [13, 17, 26, 34, 45, 62]
