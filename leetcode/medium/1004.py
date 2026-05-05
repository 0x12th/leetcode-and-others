"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
"""


def longest_ones(nums: list[int], k: int) -> int:
    zeros, res, left = 0, 0, 0
    for r, right in enumerate(nums):
        if right == 0:
            while zeros >= k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            zeros += 1
        res = max(r - left + 1, res)
    return res
