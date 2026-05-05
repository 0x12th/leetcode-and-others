"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


def product_except_self(nums: list[int]) -> list[int]:
    left = [1 for _ in range(len(nums))]
    right = left[:]

    for i in range(1, len(nums)):
        left[i] = nums[i - 1] * left[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]

    return [left[i] * right[i] for i in range(len(nums))]
