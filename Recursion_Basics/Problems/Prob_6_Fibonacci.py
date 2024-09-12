def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    nums = [1, 20, 13, 10]
    for i in nums:
        print(fib(i))
    