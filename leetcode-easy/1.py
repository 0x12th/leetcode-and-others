from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for v, value in enumerate(nums):
        if value in seen:
            return [seen[value], v]
        seen[target - value] = v
    return []
