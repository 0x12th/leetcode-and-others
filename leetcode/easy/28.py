"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
"""


def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)
