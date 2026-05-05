"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true
"""

from collections import defaultdict


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    dct = defaultdict(int)

    for i, num in enumerate(nums):
        if num in dct and i - dct[num] <= k:
            return True
        dct[num] = i

    return False
