def factorial(num: int) -> int:
    if num <= 1:
        return 1
    return num * factorial(num - 1)


if __name__ == '__main__':
    N = int(input("Enter N: "))
    print("Factorial = ", factorial(N))
