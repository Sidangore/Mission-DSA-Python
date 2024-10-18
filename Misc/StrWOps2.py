class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0] * 26
        odd = [0] * 26

        for i in range(len(s1)):
            if i % 2 == 0:
                even[ord(s1[i]) - ord('a')] += 1
                even[ord(s2[i]) - ord('a')] -= 1
            else:
                odd[ord(s1[i]) - ord('a')] += 1
                odd[ord(s2[i]) - ord('a')] -= 1

        for i in range(26):
            if even[i] != 0 or odd[i] != 0:
                return False

        return True


if __name__ == '__main__':
    s1s = ["abcdba", "abe"]
    s2s = ["cabdab", "bea"]
    testcases = len(s1s)
    sol = Solution()
    for i in range(testcases):
        print(s1s[i], s2s[i], sol.checkStrings(s1s[i], s2s[i]))
