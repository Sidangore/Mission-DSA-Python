def first_occ_itr(nums, x):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arrays = [[10, 20, 30, 40, 50, 60, 70], [1, 10, 10, 10, 20, 20, 40], [10, 20, 30], [15, 15, 15]]
    xs = [20, 20, 15, 15]
    for i in range(len(xs)):
        print(first_occ_itr(arrays[i], xs[i]))
    