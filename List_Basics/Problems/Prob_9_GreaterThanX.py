def greater_x(arr, x):
    arr = [i for i in arr if i > x]
    return -1 if max(arr) <= x else min(arr)


if __name__ == '__main__':
    arr = [4, 67, 13, 12, 15]
    x = 16
    print(greater_x(arr, x))
