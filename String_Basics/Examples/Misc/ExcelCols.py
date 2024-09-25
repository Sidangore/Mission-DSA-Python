n = 701 # int(input("Enter col number: "))
res = ""
while n:
    if n % 26 == 0:
        res = (chr(ord('@') + 26)) + res
        n -= 1
    else:
        res = (chr(ord('@') + (n % 26))) + res
    n //= 26
print(res)