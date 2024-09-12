def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    nums = [[7, 8], [2, 4]]
    for i in nums:
        print(gcd(i[0], i[1]))
    