"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    return nums1[n // 2] if n % 2 else (nums1[n // 2] + nums1[n // 2 - 1]) / 2
