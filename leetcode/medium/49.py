"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for word in strs:
        lst = [0] * 26
        for char in word:
            lst[ord(char) - ord("a")] += 1
        res[tuple(lst)].append(word)
    return list(res.values())
