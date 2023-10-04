from collections import Counter
from typing import List


def single_number(nums: List[int]) -> int:
    dct = Counter(nums)
    result = sorted(dct, key=dct.get)  # type: ignore
    return result[0]


def single_number_xor(nums: List[int]) -> int:
    mask = 0
    for num in nums:
        mask ^= num
    return mask
