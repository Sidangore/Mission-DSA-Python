def print_rec(num: int):
    if num == 0:
        return
    print(num, end=" ")
    print_rec(num - 1)


if __name__ == '__main__':
    n = int(input("Enter N: "))
    print_rec(n)
