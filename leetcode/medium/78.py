"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = [[]]

    for num in nums:
        res += [r + [num] for r in res]

    return res
