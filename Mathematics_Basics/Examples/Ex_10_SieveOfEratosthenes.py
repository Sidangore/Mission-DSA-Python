""" We will be given a number N we need to print the prime numbers till N
Ex. N = 10
O/P: 2 3 5 7

Naive Solution
1. We get the N
2. from 2 to N we check for prime and print
"""


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def print_primes(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")


def sieve_of_eratosthenes(n) -> None:
    if n <= 1:
        return
    primes = [True] * (n + 1)
    i = 2
    while (i * i) <= n:
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
        i += 1
    for i in range(2, n + 1):
        if primes[i]:
            print(i, end=" ")


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").split()))
    for i in nums:
        print(sieve_of_eratosthenes(i))
