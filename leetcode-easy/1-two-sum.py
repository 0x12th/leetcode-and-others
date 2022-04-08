from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for v, value in enumerate(nums):
        if value in seen:
            return [seen[value], v]
        seen[target - value] = v
