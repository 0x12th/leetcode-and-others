import collections
from typing import DefaultDict


def count_good_substrings_1(s: str) -> int:
    res = 0
    for k, v in enumerate(s):
        if len(set(s[k : k + 3])) == 3:
            res += 1
    return res


def count_good_substrings_2(s: str) -> int:
    dct: DefaultDict[str, int] = collections.defaultdict(int)
    left, result = 0, 0

    for right, value in enumerate(s):
        dct[value] += 1
        if right - left == 3:
            dct[s[left]] -= 1
            if dct[s[left]] == 0:
                del dct[s[left]]
            left += 1

        if len(dct) == 3:
            result += 1

    return result
