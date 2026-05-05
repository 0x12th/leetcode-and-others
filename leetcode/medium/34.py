"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


def search_range(nums: list[int], target: int) -> list[int]:
    def helper(t: int):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < t:
                left = mid + 1
            else:
                right = mid
        return left

    left = helper(target)
    right = helper(target + 1) - 1

    if left <= right:
        return [left, right]

    return [-1, -1]
