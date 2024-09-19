def quick_sort(nums, low, high):
    if low < high:
        pivot = lomuto(nums, low, high)
        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)


def lomuto(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[high], nums[i + 1] = nums[i + 1], nums[high]
    return i + 1


if __name__ == '__main__':
    nums = [88, 98, 34, 38, 28, 58, 66]
    quick_sort(nums, 0, len(nums) - 1)
    print("Sorted: ", nums)
