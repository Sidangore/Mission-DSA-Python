def fun(n):
    if n < 10:
        return n
    return (n % 10) + fun(n // 10)


if __name__ == '__main__':
    n = [1, 99999]
    for i in n:
        print(fun(i))
    