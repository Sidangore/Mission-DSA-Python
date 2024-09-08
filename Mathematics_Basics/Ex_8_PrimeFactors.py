def prime_factors(num):
    print(num, ": ", end="")
    for i in range(2, num + 1):
        if is_prime(i):
            x = i
            while num % x == 0:
                print(i, end=" ")
                x = x * i


def is_prime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while (i * i) <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").split()))
    for i in nums:
        print(prime_factors(i))