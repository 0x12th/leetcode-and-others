"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true
"""


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    mapper_s_t, mapper_t_s = {}, {}
    for char_s, char_t in zip(s, t):
        if char_s in mapper_s_t and mapper_s_t[char_s] != char_t:
            return False
        if char_t in mapper_t_s and mapper_t_s[char_t] != char_s:
            return False

        mapper_s_t[char_s] = char_t
        mapper_t_s[char_t] = char_s

    return True
