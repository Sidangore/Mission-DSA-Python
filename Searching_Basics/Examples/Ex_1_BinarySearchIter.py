from typing import List


def bin_search_itr(nums: List[int], x: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if x == nums[mid]:     # Element Found at mid
            return mid
        elif x < nums[mid]:    # We can ignore the right part of mid
            high = mid - 1
        else:                  # We can ignore the left part of mid
            low = mid + 1

    return -1   # if the element is not found


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").strip().split()))
    x = int(input("Enter x: "))
    print(bin_search_itr(nums, x))

