def reverse_1(nums):
    nums.reverse()
    return nums


def reverse_2(nums):
    return list(reversed(nums))


def reverse_3(nums):
    return nums[::-1]


def reverse_4(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


if __name__ == '__main__':
    nums = list(map(int, input("Enter nums: ").strip().split()))
    print(reverse_4(nums))
    print(reverse_3(nums))
    print(reverse_2(nums))
    print(reverse_1(nums))

