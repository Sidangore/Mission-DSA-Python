def isPanagram(self, s):
    # your code here
    chars = [0] * 26
    for i in s.lower():
        chars[ord(i) - ord('a')] += 1
    for i in chars:
        if i < 1:
            return 0
    return 1