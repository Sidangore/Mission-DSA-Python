"""
S(n) = n+ n*(S(n-1)) and S(0) = 1

Write the function for this recursively
"""


def fun(n):
    if n == 0:
        return 1
    return n + (n * fun(n - 1))


if __name__ == '__main__':
    inputs = [2, 3]
    for i in inputs:
        print(fun(i))
