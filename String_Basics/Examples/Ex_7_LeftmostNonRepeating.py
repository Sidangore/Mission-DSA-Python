import sys


def fun(s):
    indexes = [-1] * 256
    res = sys.maxsize
    for i in range(len(s)):
        if indexes[ord(s[i])] == -1:
            indexes[ord(s[i])] = i
        else:
            indexes[ord(s[i])] = -2
    for i in range(len(s)):
        if indexes[ord(s[i])] >= 0:
            res = min(res, indexes[ord(s[i])])
    return -1 if res == sys.maxsize else res


def fun2(s):
    visited = [False] * 256
    res = -1
    for i in range(len(s) - 1, -1, -1):
        if not visited[ord(s[i])]:
            visited[ord(s[i])] = True
            res = i
        else:
            res = -1
    return res


s = input("Enter: ")
print(fun(s))
