from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1
