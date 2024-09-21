def sumExists(arr, sum):
    #Your code here
    s = set()
    for i in arr:
        if (sum - i) in s:
            return True
        s.add(i)
    return False


if __name__ == '__main__':
    print(sumExists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14))