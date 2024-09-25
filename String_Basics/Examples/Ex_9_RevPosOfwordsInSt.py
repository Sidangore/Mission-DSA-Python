def rev(txt, low, high):
    while low < high:
        txt[low], txt[high] = txt[high], txt[low]
        low += 1
        high -= 1


def rev_pos(line):
    n = len(line)
    line = list(line)
    low = 0
    for high in range(n):
        if line[high] == " ":
            rev(line, low, high - 1)
            low = high + 1
    rev(line, low, n - 1)
    rev(line, 0, n - 1)
    return ''.join(line)


line = input("Enter line: ")
line = rev_pos(line)
print(line)
