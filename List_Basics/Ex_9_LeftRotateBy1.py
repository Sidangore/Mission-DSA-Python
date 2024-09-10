def left_rotate_by_1_1(nums):
    return nums[1:] + nums[:1]


def left_rotate_by_1_2(nums):
    nums.append(nums.pop(0))
    return nums


def left_rotate_by_1_3(nums):
    n = len(nums)
    x = nums[0]
    for i in range(1, n):
        nums[i - 1] = nums[i]
    nums[n - 1] = x
    return nums


if __name__ == '__main__':
    nums = list(map(int, input("Enter nums: ").strip().split()))
    print(left_rotate_by_1_3(nums))
