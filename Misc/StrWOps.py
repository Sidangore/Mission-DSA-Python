class Solution:
    def check_if_strs_are_same(self, s1: str, s2: str) -> bool:
        s3, s4 = self.op(s2, 0), self.op(s2, 1)
        s5 = self.op(s3, 1)
        return s1 == s3 or s1 == s4 or s1 == s5

    def op(self, s: str, index: int):
        s = list(s)
        s[index], s[index + 2] = s[index + 2], s[index]
        return "".join(s)


if __name__ == '__main__':
    sol = Solution()
    testcases = int(input())
    while testcases > 0:
        s1, s2 = map(str, input().split())
        print(sol.check_if_strs_are_same(s1, s2))
        testcases = testcases - 1