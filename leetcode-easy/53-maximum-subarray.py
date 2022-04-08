from typing import List


def maxSubArray(nums: List[int]) -> int:
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum
