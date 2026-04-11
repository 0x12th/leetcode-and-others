def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for v, value in enumerate(nums):
        if value in seen:
            return [seen[value], v]
        seen[target - value] = v
    return []
