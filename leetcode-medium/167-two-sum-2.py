from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    seen = {}
    for n, num in enumerate(numbers, 1):
        if target - num in seen:
            return [seen[target - num], n]
        seen[num] = n
