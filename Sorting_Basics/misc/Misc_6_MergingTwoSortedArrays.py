from typing import List


def merge(arr1: List[int], arr2: List[int]):
    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    res = []

    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < m:
        res.append(arr1[i])
        i += 1

    while j < n:
        res.append(arr2[j])
        j += 1

    return res


if __name__ == '__main__':
    arr1 = [13, 17, 26, 34, 45, 62]
    arr2 = [4, 12, 13, 15, 67]
    arr3 = merge(arr1, arr2)
    print(arr3)
