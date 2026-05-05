"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
"""


def max_sub_array(nums: list[int]) -> int:
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum
