import functools


def multiply(num1: str, num2: str) -> str:
    products = []
    i, j = len(num1) - 1, len(num2) - 1

    while j >= 0:
        prd = '0' * (len(num2) - 1 - j)
        i = len(num1) - 1
        carry = 0

        while i >= 0:
            p = ((ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))) + carry
            carry = p // 10
            p %= 10
            prd = f"{p}" + prd
            i -= 1

        if carry > 0:
            prd = f"{carry}" + prd

        j -= 1
        products.append(prd)
    # print(products)
    return functools.reduce(lambda x, y: add(x, y), products)


def add(a: str, b: str) -> str:
    carry = 0
    add = ""
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 and j >= 0:
        s = carry + ord(a[i]) + ord(b[j]) - (2 * ord('0'))
        carry = s // 10
        s %= 10
        add = f"{s}" + add
        i -= 1
        j -= 1

    while i >= 0:
        s = carry + ord(a[i]) - ord('0')
        carry = s // 10
        s %= 10
        add = f"{s}" + add
        i -= 1

    while j >= 0:
        s = carry + ord(b[j]) - ord('0')
        carry = s // 10
        s %= 10
        add = f"{s}" + add
        j -= 1

    if carry > 0:
        add = f"{carry}" + add

    return add


num1, num2 = map(str, input("Enter 2 nums: ").split())
print("Multiplication: ", multiply(num1, num2))
# print("Addition: ", add("738", "6150")) # ['738', '6150', '49200']
