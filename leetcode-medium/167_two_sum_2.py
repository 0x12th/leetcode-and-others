from typing import Dict, List


def two_sum(numbers: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for n, num in enumerate(numbers, 1):
        if target - num in seen:
            return [seen[target - num], n]
        seen[num] = n
    return []
