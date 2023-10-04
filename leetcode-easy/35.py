from typing import List, Optional


def search_insert(nums: List[int], target: int) -> Optional[int]:
    left = 0
    right = len(nums) - 1
    while left <= right:
        if target > nums[right]:
            return right + 1
        if target < nums[left]:
            return left

        middle = (left + right) // 2
        middle_num = nums[middle]
        if middle_num == target:
            return middle
        if middle_num > target:
            right = middle - 1
        else:
            left = middle + 1
    return None
