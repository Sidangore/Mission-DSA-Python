def fun(n):
    if n < 10:
        return 1
    return 1 + fun(n // 10)


if __name__ == '__main__':
    nums = [1, 99999, 3432]
    for i in nums:
        print(fun(i))
    