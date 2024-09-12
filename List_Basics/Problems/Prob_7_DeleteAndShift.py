def deleteFromArray(arr, n, idx):
    for i in range(idx + 1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = 0
    return arr


if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    idx = int(input())
    print(deleteFromArray(nums, len(nums), idx))
