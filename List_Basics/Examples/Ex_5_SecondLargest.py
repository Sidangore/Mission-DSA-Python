def second_largest_1(nums):
    if len(nums) <= 1:
        return None
    largest = get_largest(nums)
    res = None
    for i in nums:
        if i != largest:
            if res is None:
                res = i
            else:
                res = max(res, i)
    return res


def get_largest(nums):
    res = nums[0]
    for i in nums:
        if res < i:
            res = i
    return res


""" Second Largest in Single Traversal
l: Largest Element. Initially, nums[0]
sl: None (Initially)

Traverse through the elements of the nums

At any given element x, below conditions can take place

1. x > l: sl = l, l = x
2. x equals l: Ignore
3. x < l:
    3.1. x <= sl: Ignore
    3.2. sl is None or x > sl: sl = x
    
Ex: 5 20 20 12 10 20 10
"""


def second_largest_2(nums):
    if len(nums) <= 1:
        return None
    l, sl = nums[0], None
    
    for i in nums:
        if i > l:
            sl = l
            l = i
        elif i != l:
            if sl is None or sl < i:
                sl = i

    return sl


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").strip().split()))
    print("Second largest: ", second_largest_2(nums))
