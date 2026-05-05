"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

Input: s = "leet2code3", k = 10
Output: "o"
"""


def decode_at_index(s: str, k: int) -> str:
    left = length = 0
    while left < len(s):
        if not s[left].isdigit():
            length += 1
        else:
            length *= int(s[left])
        left += 1
    while length >= 0:
        left -= 1
        if s[left].isdigit():
            length //= int(s[left])
            k %= length
        else:
            if length == k or k == 0:
                return s[left]
            length -= 1
    return ""
