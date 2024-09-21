def first_repeating(nums):
    s = set()
    n = len(nums)
    rep = -2
    for i in range(n - 1, -1, -1):
        if nums[i] in s:
            rep = i
        s.add(nums[i])
    return rep + 1


if __name__ == '__main__':
    nums = [1, 5, 3, 4, 3, 5, 6]
    print(first_repeating(nums))
