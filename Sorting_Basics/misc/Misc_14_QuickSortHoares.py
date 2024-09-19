from typing import List


def quick_sort(nums: List[int], low: int, high: int):
    if low < high:
        pivot = hoares(nums, low, high)
        quick_sort(nums, low, pivot)
        quick_sort(nums, pivot + 1, high)


def hoares(nums: List[int], low: int, high: int):
    i, j = low - 1, high + 1
    pivot = nums[low]

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    nums = [88, 98, 34, 38, 28, 58, 66]
    quick_sort(nums, 0, len(nums) - 1)
    print("Sorted: ", nums) # Sorted:  [28, 34, 38, 58, 66, 88, 98]