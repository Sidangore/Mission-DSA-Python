def validate(s):
    #your code here
    n = len(s)
    if n < 10:
        return 0
    special = "@#$-*"
    spl = False
    num = False
    upp = False
    low = False
    for i in s:
        if i.islower():
            low = True
        elif i.isupper():
            upp = True
        elif i.isdigit():
            num = True
        elif i in special:
            spl = True
    return 1 if low and upp and num and spl else 0