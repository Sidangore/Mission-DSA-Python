def fun(times: int):
    if times <= 0:
        exit(0)
    print("SID")
    fun(times - 1)


if __name__ == '__main__':
    num = int(input("Enter N: "))
    fun(num)
