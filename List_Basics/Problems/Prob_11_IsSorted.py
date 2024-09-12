def is_sorted(arr):
    c1 = True
    c2 = True
    n = len(arr)
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            c1 = False
            break
    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            c2 = False
            break
    return c1 or c2


if __name__ == '__main__':
    arr = [[1, 1, 2, 2, 3], [4, 2]]
    for i in arr:
        print(is_sorted(i))
