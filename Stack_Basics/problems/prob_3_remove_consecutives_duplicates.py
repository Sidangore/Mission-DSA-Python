class Solution:

    # Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self, s):
        # code here
        stack = []
        stack.append(s[0])

        for ch in s[1:]:
            if stack[-1] == ch:
                continue
            else:
                stack.append(ch)

        res = ""
        while stack:
            res += stack.pop()

        return res[::-1]