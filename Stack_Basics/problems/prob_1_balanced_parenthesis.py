class Solution:

    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        open_to_close_map = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for bracket in x:
            if bracket in open_to_close_map:
                stack.append(open_to_close_map[bracket])
            else:
                if len(stack) == 0 or stack[-1] != bracket:
                    return False
                stack.pop()

        return len(stack) == 0