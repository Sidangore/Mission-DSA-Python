from typing import List


def count_inversions(nums: List[int]) -> int:
    return get_count(nums, 0, len(nums) - 1)


def get_count(nums: List[int], low: int, high: int) -> int:
    count = 0

    if low < high:
        mid = low + (high - low) // 2
        count += get_count(nums, low, mid)
        count += get_count(nums, mid + 1, high)
        count += merge_count(nums, low, mid, high)

    return count


def merge_count(nums: List[int], low: int, mid: int, high: int) -> int:
    count = 0
    left = nums[low:mid + 1]
    right = nums[mid + 1:high + 1]
    i, j = 0, 0
    m, n = len(left), len(right)
    k = low

    while i < m and j < n:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            count += m - i
            j += 1
        k += 1

    while i < m:
        nums[k] = left[i]
        k += 1
        i += 1

    while j < n:
        nums[k] = right[j]
        k += 1
        j += 1

    return count


if __name__ == '__main__':
    nums = [88, 98, 34, 38, 28, 58, 66]
    count = count_inversions(nums)
    print(count)
