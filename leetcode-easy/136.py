from collections import Counter
from typing import List


def single_number(nums: List[int]) -> int:
    dct = Counter(nums)
    result = sorted(dct, key=dct.get)  # type: ignore
    return result[0]
