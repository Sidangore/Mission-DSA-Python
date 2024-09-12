def pali(n):
    n = str(n)
    return 1 if n == n[::-1] else 0


def pali_2(n):
    n = str(n)
    i, j = 0, len(n) - 1

    def p(n, i, j):
        if i >= j:
            return True
        return n[i] == n[j] and p(n, i + 1, j - 1)

    return p(n, i, j)


if __name__ == '__main__':
    n = [100, 1001, 203202]
    for i in n:
        print(pali_2(i))

