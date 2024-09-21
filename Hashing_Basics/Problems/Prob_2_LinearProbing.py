from typing import List


def linearProbing(hashSize: int, arr: List[int], sizeOfArray: int):
    table = [-1 for _ in range(hashSize)]
    size = 0
    for value in arr:
        index = value % hashSize
        while True:
            if table[index] == -1:
                table[index] = value
                size += 1
                break
            elif table[index] == value:
                break
            index = (index + 1) % hashSize
        if size == hashSize:
            break

    return table


if __name__ == '__main__':
    nums = [4, 14, 24, 44]
    l = len(nums)
    hs = 10
    linearProbing(hs, nums, l)
