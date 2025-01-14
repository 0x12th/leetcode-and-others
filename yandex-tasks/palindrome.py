"""
'Do geese see God?' -> True
'Madam, I’m Adam' -> True
'А роза упала на лапу Азора' -> True
"""

from string import punctuation as pncts  # !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~


def check_1(s: str) -> bool:
    return s.lower() == s[::-1].lower()


def check_2(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while right >= left:
        if s[left] or s[right] in (" ", pncts):
            pass
        else:
            if s[right].lower() != s[left].lower():
                return False
        right -= 1
        left += 1
    return True
