"""
Given: N
To-do: Print number 1, 2, ..., N recursively
"""


def fun(n: int):
    if n <= 0:
        return
    fun(n - 1)
    print(n, end=" ")


if __name__ == '__main__':
    n = [10, 5]
    for i in n:
        print(fun(i))
