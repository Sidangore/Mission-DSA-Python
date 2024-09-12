"""Check if is Sorted

Traverse nums,
    if previous element is greater than current element,
    then return false
"""


def is_sorted_1(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False
    return True


""" Using the Built in Function

Get the sorted referece, 
    Compare the original and sorted list
"""


def is_sorted_2(nums):
    sl = sorted(nums)
    return sl == nums


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").strip().split()))
    print(is_sorted_1(nums))
    print(is_sorted_2(nums))

