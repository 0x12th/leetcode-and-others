import collections
from typing import List


def majority_element(nums: List[int]) -> List[int]:
    dct = collections.Counter(nums)
    return [k for k, v in dct.items() if v > len(nums) / 3]
