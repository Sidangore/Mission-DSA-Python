def selection_sort(l):
    n = len(l)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]


if __name__ == '__main__':
    l = [2, 10, 3, 1, 5, 4]
    print(l)
    selection_sort(l)
    print(l)
    
