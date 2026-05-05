"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.

Input: n = 2
Output: 1
"""


def integer_break(n: int) -> int:
    if n <= 3:
        return n - 1
    quotient, remainder = divmod(n, 3)
    if remainder == 0:
        return 3**quotient
    if remainder == 1:
        return 3 ** (quotient - 1) * 4
    return 3**quotient * remainder
