def rev_words(s):
    return " ".join([rev(word) for word in s.split()])


def rev(s):
    l = list(s)
    low, high = 0, len(s) - 1
    while low < high:
        l[low], l[high] = l[high], l[low]
        low += 1
        high -= 1
    return "".join(l)


line = input("Enter the string: ")
print(rev_words(line))
