"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
"""


def removeOccurrences(s: str, part: str) -> str:
    part_, len_part = list(part), len(part)
    res = []

    for char in s:
        res.append(char)
        if len(res) >= len_part and res[-len_part:] == part_:
            del res[-len_part:]

    return "".join(res)
