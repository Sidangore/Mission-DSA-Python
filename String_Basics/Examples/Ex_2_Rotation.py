def is_rotated(s1, s2):
    return "No" if (s1 + s1).find(s2) == -1 else "Yes"


s1, s2 = map(str, input("Enter strs: ").split())
print(is_rotated(s1, s2))
