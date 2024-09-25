def rev(s):
    r = ""
    for i in s:
        r = i + r
    return r


s = input("Enter str: ")
print(f"Reverse of {s} is {rev(s)}")