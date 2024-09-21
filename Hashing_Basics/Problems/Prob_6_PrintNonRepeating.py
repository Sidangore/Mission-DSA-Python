def print_non_repeating(arr):
    m = dict()
    for i in arr:
        if i not in m:
            m[i] = 0
        m[i] += 1
    res = []
    for i in arr:
        if m[i] == 1:
            res.append(i)
    return res


if __name__ == '__main__':
    nums = [10,20,40,30,10]
    print(print_non_repeating(nums))