def isAnagram(self, a, b):
    # code here
    m, n = len(a), len(b)
    if m != n:
        return False
    chars = [0] * 26
    for i in range(m):
        chars[ord(a[i]) - ord('a')] += 1
        chars[ord(b[i]) - ord('a')] -= 1
    for i in chars:
        if i != 0:
            return False
    return True