from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    return nums1[n // 2] if n % 2 else (nums1[n // 2] + nums1[n // 2 - 1]) / 2
