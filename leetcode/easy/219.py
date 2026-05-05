from collections import defaultdict


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    dct = defaultdict(int)

    for i, num in enumerate(nums):
        if num in dct and i - dct[num] <= k:
            return True
        dct[num] = i

    return False
