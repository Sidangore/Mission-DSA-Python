def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    a, b = map(int, input("Enter a & b: ").split())
    print("GCD: ", gcd(a, b))