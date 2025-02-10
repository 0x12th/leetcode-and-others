from collections import defaultdict


"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    color_count_map: dict[int, int] = defaultdict(int)
    for num in nums:
        color_count_map[num] += 1

    pointer = 0
    for color in range(3):
        count = color_count_map[color]
        nums[pointer : pointer + count] = [color] * count
        pointer += count
