def merge_sort(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = arr[low: mid + 1]
    right = arr[mid + 1: high + 1]
    i, j = 0, 0
    m, n = len(left), len(right)
    k = low

    while i < m and j < n:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < m:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < n:
        arr[k] = right[j]
        k += 1
        j += 1


if __name__ == '__main__':
    l = [2, 10, 3, 10, 5, 4]
    print(l)
    merge_sort(l, 0, len(l) - 1)
    print(l)
