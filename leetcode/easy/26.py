"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    res = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[res] = nums[i]
            res += 1

    return res
