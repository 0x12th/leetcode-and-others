from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    i = 0

    while i < len(nums):
        position = nums[i] - 1
        if nums[i] == nums[position]:
            i += 1
        else:
            nums[i], nums[position] = nums[position], nums[i]

    return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]
