"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
"""


def find_duplicates(nums: list[int]) -> list[int]:
    rs = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] < 0:
            rs.append(num)
        else:
            nums[num - 1] = -nums[num - 1]
    return rs
