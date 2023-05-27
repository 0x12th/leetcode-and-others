from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    zeros, res, left = 0, 0, 0
    for r, right in enumerate(nums):
        if right == 0:
            while zeros >= k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            zeros += 1
        res = max(r - left + 1, res)
    return res
