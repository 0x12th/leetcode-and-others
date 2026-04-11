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
