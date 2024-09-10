def get_odd_occurring(nums):
    res = 0
    for i in nums:
        res ^= i
    return res


if __name__ == '__main__':
    nums = list(map(int, input("Enter nums: ").strip().split()))
    print(get_odd_occurring(nums))
