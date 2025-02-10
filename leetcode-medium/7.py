"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321
"""


def reverse(x: int) -> int:
    rev_str = str(abs(x))[::-1]
    rev_int = -int(rev_str) if x < 0 else int(rev_str)

    if rev_int > 2**31 - 1 or rev_int < -(2**31):
        return 0

    return rev_int
