from typing import List


def average(l: List[int]) -> float:
    return sum(l) / len(l)


if __name__ == "__main__":
    l: List[int] = [10, 20, 30, 40]
    print("Average = ", average(l))
