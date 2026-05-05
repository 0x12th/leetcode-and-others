"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
"""


def missing_number(nums: list[int]) -> int:
    len_nums = len(nums)
    return len_nums * (len_nums + 1) // 2 - sum(nums)
