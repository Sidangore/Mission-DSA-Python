def fun(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return fun(n // 2)
    return fun(n // 2) + fun((n // 2) + 1)

if __name__ == '__main__':
    print(fun(11))