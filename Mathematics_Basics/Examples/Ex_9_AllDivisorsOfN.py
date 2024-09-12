"""
Time Complexity = Theta (N)
Auxiliary Space = O(1)
"""


def all_divisors(n):
    print(n, ":", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")


"""
Divisors of a number always appears in Pair (x, y)
"""


def all_divisors_eff(n):
    print(n, ":", end=" ")
    i = 1
    while (i * i) < n:
        if n % i == 0:
            print(i, end=" ")
        i += 1
    while i >= 1:
        if n % i == 0:
            print(n//i, end=" ")
        i -= 1


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").split()))
    for i in nums:
        print(all_divisors(i))
        print(all_divisors_eff(i))
