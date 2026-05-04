"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break

        if nums[i] + nums[n - 2] + nums[n - 1] < 0:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1

    return res
