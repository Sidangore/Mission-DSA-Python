def fun(x, y):
    if x == 0:
        return y
    return fun(x - 1, x + y)


if __name__ == '__main__':
    print(fun(4, 3))
    print(1000 > 1000)


"""
(11)
(5 + 6)
(2 + 3) + (3 + 4)
((1) + (1) + (1)) + ((1) + (1) + (1))
     
"""