"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    res = []

    def helper(current: list[int], used: list[int]):
        if len(nums) == len(current):
            res.append(current[:])
            return
        for num in range(len(nums)):
            if not used[num]:
                current.append(nums[num])
                used[num] = True
                helper(current, used)
                current.pop()
                used[num] = False

    helper([], [False] * len(nums))

    return res
