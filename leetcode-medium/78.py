def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = [[]]

    for num in nums:
        res += [r + [num] for r in res]

    return res
