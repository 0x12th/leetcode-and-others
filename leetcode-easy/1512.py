from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        n = i
        while n <= len(nums) - 2:
            n += 1
            if nums[i] == nums[n]:
                res += 1
    return res
