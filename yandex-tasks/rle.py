"""
"AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB" -> "A4B3C2XYZD4E3F3A6B28"
"""


import string


def rle(s: str) -> str:
    if len(s) == 0:
        return ""
    result = []
    last_letter = s[0]
    count = 0

    for letter in s:
        if letter not in string.ascii_letters:
            return "Not valid string."
        if last_letter and letter != last_letter:
            if count == 1:
                result.append(last_letter)
            else:
                result.append(last_letter + str(count))
            count = 1
            last_letter = letter
        else:
            count += 1
    if count == 1:
        result.append(last_letter)
    else:
        result.append(last_letter + str(count))
    return "".join(result)
