def remove_dup(nums):
    n = len(nums)
    temp = [0] * n
    temp[0] = nums[0]
    size = 1
    for i in range(1, n):
        if temp[size - 1] != nums[i]:
            temp[size] = nums[i]
            size += 1
    nums[:size] = temp[:size]
    return nums, size


def remove_dup_2(nums):
    size = 1
    for i in range(1, len(nums)):
        if nums[size - 1] != nums[i]:
            nums[size] = nums[i]
            size += 1
    return nums, size


if __name__ == '__main__':
    nums = list(map(int, input("Enter nums: ").strip().split()))
    print(remove_dup_2(nums))
