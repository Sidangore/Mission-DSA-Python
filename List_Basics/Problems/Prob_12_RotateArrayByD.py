def rotate_d(arr, d):
    rev(arr, 0, d)
    rev(arr, d, len(arr))
    rev(arr, 0, len(arr))
    print(arr)


def rev(arr, start, end):
    end -= 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    d = 3
    print(rotate_d(arr, d))
