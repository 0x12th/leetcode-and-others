def two_sum(numbers: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for n, num in enumerate(numbers, 1):
        if target - num in seen:
            return [seen[target - num], n]
        seen[num] = n
    return []
