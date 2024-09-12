def rev(arr, n):
    start = 0
    end = n - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    arrays = [[1, 1, 2, 2, 3], [4, 2]]
    for arr in arrays:
        print("Before: ", arr)
        rev(arr, len(arr))
        print("After: ", arr)
