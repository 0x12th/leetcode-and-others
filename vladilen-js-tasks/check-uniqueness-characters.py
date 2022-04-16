# abcdef -> True
# 1234567 -> True
# abcABC -> True
# abcadef -> False


from collections import defaultdict, Counter


def is_unique_0(s: str) -> bool:
    dct = {}
    for value in s:
        if value not in dct:
            dct[value] = 0
        dct[value] += 1
        if dct[value] > 1:
            return False
    return True


def is_unique_1(s: str) -> bool:
    dct = defaultdict(int)
    for value in s:
        dct[value] += 1
        if dct[value] > 1:
            return False
    return True


def is_unique_2(s: str) -> bool:
    dct = Counter(s)
    for _ in dct:
        if dct[_] > 1:
            return False
    return True
