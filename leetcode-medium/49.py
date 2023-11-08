from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for word in strs:
        lst = [0] * 26
        for char in word:
            lst[ord(char) - ord("a")] += 1
        res[tuple(lst)].append(word)
    return list(res.values())
