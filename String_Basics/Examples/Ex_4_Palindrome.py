def is_pali(s):
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


def pali(s):
    if s == s[::-1]:
        return True
    return False


s = input("Enter string: ")
print(f"String: {s} {is_pali(s)}")