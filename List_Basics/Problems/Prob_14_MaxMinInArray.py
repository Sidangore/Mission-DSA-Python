def max_element(arr, n):
    return max(arr)


def max_1(arr):
    n = len(arr)
    if n == 0:
        return None
    res = arr[0]
    for i in arr[1:]:
        if i > res:
            res = i
    return res


def min_element(arr, n):
    return min(arr)


def min_1(arr):
    n = len(arr)
    if n == 0:
        return None
    res = arr[0]
    for i in arr[1:]:
        if i < res:
            res = i
    return res


if __name__ == '__main__':
    arrays = [[1, 1, 2, 2, 3], [4, 2], [5, 4, 2, 1], [8]]
    for arr in arrays:
        print(arr, ", max = ", max_1(arr), ", min = ", min_1(arr))
    