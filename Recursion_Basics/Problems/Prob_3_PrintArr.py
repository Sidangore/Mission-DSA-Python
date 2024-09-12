"""
Given An array of numbers
Tasks: Print Array Elements using Recursion
"""
from typing import List


def fun(nums: List[int], n: int):
    if n == 0:
        return
    print(nums[len(nums) - n], end=" ")
    fun(nums, n - 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    fun(arr, 5)
    