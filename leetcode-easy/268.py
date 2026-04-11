def missing_number(nums: list[int]) -> int:
    len_nums = len(nums)
    return len_nums * (len_nums + 1) // 2 - sum(nums)
