from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def helper(current: List[int], used: List[int]):
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
