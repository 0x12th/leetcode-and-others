"""
'Do geese see God?' -> True
'Madam, I’m Adam' -> True
'А роза упала на лапу Азора' -> True
"""

from string import punctuation as pncts  # !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~


def _check_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while j > i:
        rev_ch = s[j]
        ch = s[i]
        if not rev_ch.isalpha():
            j -= 1
            continue
        if not ch.isalpha():
            i += 1
            continue
        if rev_ch.lower() != ch.lower():
            return False
        j -= 1
        i += 1
    return True


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
