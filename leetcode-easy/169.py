from collections import defaultdict


def majority_element(nums: list[int]) -> int:
    dct: dict[int, int] = defaultdict(int)
    most_common = nums[0] if len(nums) > 0 else 0
    for i in nums:
        dct[i] += 1
        if dct[most_common] < dct[i]:
            most_common = i
    return most_common
