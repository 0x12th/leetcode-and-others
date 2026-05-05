"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
"""

from collections import defaultdict


def majority_element(nums: list[int]) -> int:
    dct: dict[int, int] = defaultdict(int)
    most_common = nums[0] if len(nums) > 0 else 0
    for i in nums:
        dct[i] += 1
        if dct[most_common] < dct[i]:
            most_common = i
    return most_common
