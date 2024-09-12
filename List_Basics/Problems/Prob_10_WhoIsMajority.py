def majority(nums, x, y):
    c1, c2 = nums.count(x), nums.count(y)
    if c1 == c2:
        return x if x < y else y
    return x if c1 > c2 else y