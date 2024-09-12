def is_pal(n):
    rev = 0
    temp = n

    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp //= 10

    return rev == n


if __name__ == '__main__':
    n = int(input("Enter n: "))
    print(is_pal(n))
