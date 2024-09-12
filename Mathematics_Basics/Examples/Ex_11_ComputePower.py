def pow(x, n) -> int:
    temp = x
    if n == 0:
        return 1
    for _ in range(1, n + 1):
        temp *= x
    return temp


def power_rec(x, n) -> int:
    if n == 0:
        return 1
    temp = power_rec(x, n // 2)
    temp = temp * temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x

if __name__ == '__main__':
    nums = list(map(int, input("Enter nums: ").split()))
    for i in nums:
        print(f'{i}: {power_rec(i, 3)}')
