from typing import List


def missing_number(nums: List[int]) -> int:
    len_nums = len(nums)
    return len_nums * (len_nums + 1) // 2 - sum(nums)
