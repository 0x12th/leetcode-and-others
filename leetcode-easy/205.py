"""
s = "egg", t = "add" --> True
s = "foo", t = "bar" --> False
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
