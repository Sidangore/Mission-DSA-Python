def get_ele(arr, i):
    return arr[i] if i < len(arr) else -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(get_ele(arr, 4))

