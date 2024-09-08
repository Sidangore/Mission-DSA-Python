def fact_itr(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)


if __name__ == '__main__':
    num = int(input("Enter num: "))
    print("Factorial: ", fact_itr(num))
    print("Factorial: ", fact_rec(num))
