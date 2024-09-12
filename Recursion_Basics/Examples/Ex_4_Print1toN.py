def print_rec(num: int):
    if num == 0:
        return
    print_rec(num - 1)
    print(num, end=" ")


if __name__ == '__main__':
    n = int(input("Enter N: "))
    print_rec(n)
