def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)


if __name__ == '__main__':
    nums = [[5, 2], [4, 1]]
    for i in nums:
        print(nCr(i[0], i[1]))

