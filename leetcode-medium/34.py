from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    def helper(t: int):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < t:
                left = mid + 1
            else:
                right = mid
        return left

    left = helper(target)
    right = helper(target + 1) - 1

    if left <= right:
        return [left, right]

    return [-1, -1]
