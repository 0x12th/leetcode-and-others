"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
"""


def is_happy(n: int) -> bool:
    if n == 1:
        return True
    if n == 4:
        return False
    return is_happy(sum([n**2 for n in [int(i) for i in str(n)]]))
