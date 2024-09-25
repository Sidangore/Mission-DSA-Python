def missingPanagram(self, s):
    s = s.lower()
    chars = [0] * 26
    res = ""
    for i in s:
        chars[ord(i) - ord('a')] += 1
    for i in range(26):
        if chars[i] == 0:
            res += chr(ord('a') + i)
    return -1 if res == "" else res