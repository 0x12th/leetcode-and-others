"""
'abcd' -> 'abcd'
'aabbccdd' -> 'abcd'
'abcddbca' -> 'abcd'
'abababcdcdcd' -> 'abcd'
"""

from collections import Counter


def remove_dupes_1(s: str) -> str:
    return "".join(set(s))


def remove_dupes_2(s: str) -> str:
    return "".join(Counter(s))
