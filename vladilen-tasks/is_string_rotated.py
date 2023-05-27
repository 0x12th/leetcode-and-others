"""
('javascript', 'scriptjava') -> true
('javascript', 'iptjavascr') -> true
('javascript', 'java') -> false
"""


import collections


def is_string_rotated(str1: str, str2: str) -> bool:
    return collections.Counter(str1) == collections.Counter(str2)
