def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        x = l[i]
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = x


if __name__ == '__main__':
    l = [2, 10, 3, 10, 5, 4]
    print(l)
    insertion_sort(l)
    print(l)