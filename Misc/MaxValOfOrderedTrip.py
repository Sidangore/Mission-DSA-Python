from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n
        res = -1

        prefix_max[0], suffix_max[n - 1] = nums[0], nums[n - 1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        for j in range(1, n - 1):
            res = max(res, (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1])
        # print("Array: ", nums, "Prefix: ", prefix_max, "Suffix: ", suffix_max)
        return 0 if res < 0 else res


if __name__ == '__main__':
    tcs = [[12, 6, 1, 2, 7], [1, 10, 3, 4, 19], [1, 2, 3]]
    sol = Solution()
    for tc in tcs:
        print(sol.maximumTripletValue(tc))
