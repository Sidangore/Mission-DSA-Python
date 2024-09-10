import functools


def get_largest(nums):
    res = nums[0]
    for i in nums:
        if i > res:
            res = i
    return res


def get_largest_2(nums):
    return max(nums)


def get_largest_3(nums):
    return functools.reduce(lambda x, y: x if x > y else y, nums)


if __name__ == '__main__':
    nums = [10, 20, 5, 50]
    print(get_largest_3(nums))
    print(get_largest_2(nums))
    print(get_largest(nums))
