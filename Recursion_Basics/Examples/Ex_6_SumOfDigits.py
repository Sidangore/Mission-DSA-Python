def sum_digits(num: int) -> int:
    if num < 10:
        return num
    return (num % 10) + sum_digits(num // 10)


if __name__ == '__main__':
    n = int(input("Enter N: "))
    print("Sum of digits = ", sum_digits(n))
