import sys


def fun(s):
    rep = sys.maxsize
    indexes = [-1] * 256

    for i in range(len(s)):
        if indexes[ord(s[i])] == -1:
            indexes[ord(s[i])] = i
        else:
            rep = min(rep, indexes[ord(s[i])])

    return -1 if rep == sys.maxsize else rep


def fun2(s):
    visited = [False] * 256
    res = -1
    for i in range(len(s) - 1, -1, -1):
        if visited[ord(s[i])]:
            res = i
        else:
            visited[ord(s[i])] = True
    return res


s = input("Enter String: ")
print(fun2(s))

