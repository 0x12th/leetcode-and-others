"""
[1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2] -> [1, 2, 2, 3]
"""

from collections import defaultdict


def common_elements(a: list[int], b: list[int]) -> list[int]:
    b_dict: defaultdict[int, int] = defaultdict(int)
    for el in b:
        b_dict[el] += 1
    result = []
    for el in a:
        count = b_dict[el]
        if count > 0:
            result.append(el)
            b_dict[el] -= 1
    return result
