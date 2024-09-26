from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        # print("Converting all smaller and greater values to n + 1: ", nums)
        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1
            if nums[val] > 0:
                nums[val] = -1 * nums[val]

        # print("Converting all numbers in range to negative at index: ", nums)

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


if __name__ == '__main__':
    sol = Solution()

    inputs = [[1, 2, 3, 4], [1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [2147483647,2147483646,2147483645,3,2,1,-1,0,-2147483648]]
    for nums in inputs:
        print("nums: ", nums)
        print(sol.firstMissingPositive(nums))

