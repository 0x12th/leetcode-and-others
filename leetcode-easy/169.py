from collections import defaultdict
from typing import Dict, List


def majority_element(nums: List[int]) -> int:
    dct: Dict[int, int] = defaultdict(int)
    most_common = nums[0] if len(nums) > 0 else 0
    for i in nums:
        dct[i] += 1
        if dct[most_common] < dct[i]:
            most_common = i
    return most_common
