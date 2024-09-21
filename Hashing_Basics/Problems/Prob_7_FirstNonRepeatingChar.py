def first_non_repeating(txt):
    m = dict()
    for i in txt:
        if i not in m:
            m[i] = 0
        m[i] += 1
    for i in txt:
        if m[i] == 1:
            return i
    return -1


print(first_non_repeating("zxvczbtxyzvy"))