def fibonacci(num: int) -> int:
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    N = int(input("Enter N: "))
    print("Nth Fibonacci = ", fibonacci(N))
