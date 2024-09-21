def countNonRepeated(arr):
    m = dict()
    for i in arr:
        if i not in m:
            m[i] = 0
        m[i] += 1
    count = 0
    for i in m.values():
        if i == 1:
            count += 1
    return count


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(countNonRepeated(nums))