class Solution:

    # Function to remove pair of duplicates from given string using Stack.
    def removePair(self, s):
        # code here
        stack = []
        for ch in s:
            if len(stack) != 0 and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        res = ""
        while stack:
            res += stack.pop()

        return "Empty String" if res == "" else res[::-1]