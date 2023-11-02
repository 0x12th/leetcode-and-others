def length_of_last_word(self, s: str) -> int:
    if len(s) == 1:
        return len(s)
    len_last = 0
    letter = len(s) - 1
    while letter >= 0:
        if s[letter] != " ":
            len_last += 1
        if s[letter] == " " and len_last != 0:
            return len_last
        letter -= 1
    return len_last
