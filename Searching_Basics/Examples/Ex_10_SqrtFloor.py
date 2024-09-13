def sqroot_floor(n):
    low, high = 0, n
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        msq = mid * mid

        if msq == n:
            return mid
        elif msq < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


if __name__ == '__main__':
    inputs = [20, 25, 15, 75, 20, 10, 7, 10]
    for i in inputs:
        print(i, ": ", sqroot_floor(i))
