def subseq(s1, s2):
    j = 0

    for i in s1:
        if i == s2[j]:
            j += 1
    return j == len(s2)


s1, s2 = map(str, input("Enter strings: ").strip().split())
print(subseq(s1, s2))
