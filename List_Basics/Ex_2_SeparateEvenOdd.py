def get_even_odd(l):
    even = [x for x in l if x % 2 == 0]
    odd = [x for x in l if x not in even]
    return even, odd


if __name__ == '__main__':
    l = [10, 41, 30, 15, 80]
    print(get_even_odd(l))
