from collections import Counter


def single_number(nums: list[int]) -> int:
    dct = Counter(nums)
    result = sorted(dct, key=dct.get)  # type: ignore
    return result[0]


def single_number_xor(nums: list[int]) -> int:
    mask = 0
    for num in nums:
        mask ^= num
    return mask
