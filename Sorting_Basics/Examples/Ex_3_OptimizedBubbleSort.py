def bubble_sort(l):
    n = len(l)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            return


if __name__ == '__main__':
    l = [2, 10, 3, 1, 5, 4]
    print(l)
    bubble_sort(l)
    print(l)
