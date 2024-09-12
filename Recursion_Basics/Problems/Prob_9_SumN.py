def fun(n):
    if n < 1:
        return 0
    return n + fun(n - 1)


if __name__ == '__main__':
    n = [5, 4, 10]
    for i in n:
        print(fun(i))
    