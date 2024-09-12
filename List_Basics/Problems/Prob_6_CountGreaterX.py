def count_ele(arr, x):
    return len([i for i in arr if i > x])


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 2, 2, 2, 2]
    x = 3
    print(count_ele(arr, x))
