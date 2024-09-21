def freq(arr):
    m = dict()
    for i in arr:
        if i not in m:
            m[i] = 0
        m[i] += 1
    for i in m:
        print(i, m[i])


if __name__ == '__main__':
    freq([10, 12, 10, 15, 10, 20, 12, 12])
