from typing import List


def get_smaller_elements(nums: List[int], x: int) -> List[int]:
    return [i for i in nums if i < x]


if __name__ == "__main__":
    nums = [8, 100, 20, 40, 3, 7, 60, 80, 200]
    x = 60
    print(get_smaller_elements(nums, x))
