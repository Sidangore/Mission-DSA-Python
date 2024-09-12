def smaller(arr, x):
    if x <= min(arr):
        return -1
    return max([i for i in arr if i < x])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    x = 1
    print(smaller(arr, x))
