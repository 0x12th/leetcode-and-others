"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    i = 0

    while i < len(nums):
        position = nums[i] - 1
        if nums[i] == nums[position]:
            i += 1
        else:
            nums[i], nums[position] = nums[position], nums[i]

    return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]
