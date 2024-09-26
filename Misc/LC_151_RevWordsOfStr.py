def reverseWords(s: str) -> str:
    res = []
    start, end = 0, 0
    n = len(s)

    while end < n:
        while end < n and s[end] == " ":
            end += 1
        if end == n:
            break
        start = end
        while end < n and s[end] != " ":
            end += 1
        res.append(s[start:end])
        print(res)

    return " ".join(res[::-1])


def rev(s: str, low: int, high: int):
    while low < high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    return s[low:high + 1]


if __name__ == '__main__':
    strs = ["  hello world  "] # , "a good   example" , "the sky is blue"
    for s in strs:
        print(reverseWords(s))
