def merge_arr(a ,b):
    n, m = len(a), len(b)
    i, j = 0, 0
    res = []

    while i < n and j < m:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < n:
        res.append(a[i])
        i += 1

    while j < m:
        res.append(b[j])
        j += 1

    return res


if __name__ == '__main__':
    a = [10, 15, 20]
    b = [5, 6, 6, 30]
    res = merge_arr(a, b)
    print(res)
