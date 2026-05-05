"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Input: nums = [3,2,3]
Output: [3]
"""

import collections


def majority_element(nums: list[int]) -> list[int]:
    dct = collections.Counter(nums)
    return [k for k, v in dct.items() if v > len(nums) / 3]
