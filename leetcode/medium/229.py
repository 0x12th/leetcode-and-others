import collections


def majority_element(nums: list[int]) -> list[int]:
    dct = collections.Counter(nums)
    return [k for k, v in dct.items() if v > len(nums) / 3]
