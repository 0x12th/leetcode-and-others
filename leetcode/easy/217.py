def contains_duplicate(nums: list[int]) -> bool:
    set_nums = set(nums)
    return len(nums) > len(set_nums)
