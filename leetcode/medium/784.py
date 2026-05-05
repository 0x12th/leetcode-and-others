"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
"""


def letter_case_permutation(s: str) -> list[str]:
    result = []

    def helper(curr, s, i):
        if len(curr) == len(s):
            result.append(curr)
            return

        helper(curr + s[i], s, i + 1)

        if s[i].isalpha():
            helper(curr + s[i].swapcase(), s, i + 1)
        return

    helper("", s, 0)

    return result
