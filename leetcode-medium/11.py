from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        min_height = min(height[left], height[right])
        max_area = max(max_area, min_height * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
