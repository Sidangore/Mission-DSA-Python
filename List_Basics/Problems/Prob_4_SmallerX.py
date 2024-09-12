def count_small(arr, x):
    return len([i for i in arr if i < x])


if __name__ == '__main__':
    arr = [[4, 5, 3, 1, 2], [2, 2, 2, 2, 2, 2, 2]]
    x = [2, 3]
    for i in range(len(x)):
        print(count_small(arr[i], x[i]))

