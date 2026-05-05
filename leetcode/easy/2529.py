"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
"""


def maximum_count(nums: list[int]) -> int:  # O(n)
    pos_count = neg_count = 0
    for num in nums:
        if num > 0:
            pos_count += 1
        if num < 0:
            neg_count += 1

    return max(pos_count, neg_count)


def maximum_count_log_n(nums: list[int]) -> int:  # O(log n)
    def first_index(find_positive):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if find_positive:
                if nums[mid] > 0:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] >= 0:
                    right = mid
                else:
                    left = mid + 1
        return left

    neg = first_index(False)
    pos = len(nums) - first_index(True)

    return max(neg, pos)
