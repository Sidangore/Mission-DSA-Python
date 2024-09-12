def trailing_zeroes(n) -> int:
    if n < 0:
        return -1
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers: ").split()))
    for i in nums:
        print(trailing_zeroes(i))
