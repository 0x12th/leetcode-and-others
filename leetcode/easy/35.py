"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""


def search_insert(nums: list[int], target: int) -> int | None:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if target > nums[right]:
            return right + 1
        if target < nums[left]:
            return left

        middle = (left + right) // 2
        middle_num = nums[middle]
        if middle_num == target:
            return middle
        if middle_num > target:
            right = middle - 1
        else:
            left = middle + 1
    return None
