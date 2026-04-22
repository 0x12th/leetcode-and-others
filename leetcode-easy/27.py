"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
"""


def remove_element(nums: list[int], val: int) -> int:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)

    return len(nums)
