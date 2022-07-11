# ['a', 'b', 'c', 'c', 'd', 'e'] -> c
# ['abc', 'def', 'abc', 'def', 'abc'] -> abc
# ['abc', 'def'] -> abc
# ['abc', 'abc', 'def', 'def', 'def', 'ghi', 'ghi', 'ghi', 'ghi' ] -> ghi


import collections


def get_highest_freq_str(lst: list[str]) -> str:
    dct = collections.defaultdict(int)
    result = ""
    max_freq = 0
    for v in lst:
        dct[v] += 1
        if dct[v] > max_freq:
            max_freq = dct[v]
            result = v
    return result
