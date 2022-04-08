from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    set_nums = set(nums)
    return True if len(nums) > len(set_nums) else False
