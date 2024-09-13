from typing import List


def bin_search_rec(nums: List[int], x: int, low: int, high: int) -> int:
    if low <= high:
        mid = (low + high) // 2
        if x == nums[mid]:
            return mid
        elif x < nums[mid]:
            return bin_search_rec(nums, x, low, mid - 1)
        else:
            return bin_search_rec(nums, x, mid + 1, high)
    return -1


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").strip().split()))
    x = int(input("Enter x: "))
    print(bin_search_rec(nums, x, 0, len(nums) - 1))
