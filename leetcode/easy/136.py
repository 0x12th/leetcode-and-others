"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1
"""

from collections import Counter


def single_number(nums: list[int]) -> int:
    dct = Counter(nums)
    result = sorted(dct, key=dct.get)  # type: ignore
    return result[0]


def single_number_xor(nums: list[int]) -> int:
    mask = 0
    for num in nums:
        mask ^= num
    return mask
