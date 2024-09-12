def fact(n):
    if n <= 0:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    n = [5, 4, 0]
    for i in n:
        print(fact(i))
    
