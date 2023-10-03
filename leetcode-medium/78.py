from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = [[]]

    for num in nums:
        res += [r + [num] for r in res]

    return res
