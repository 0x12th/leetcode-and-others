"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Input: x = 121
Output: true
"""


def is_palindrome(x: int) -> bool:
    return list(str(x)) == list(reversed(str(x)))
