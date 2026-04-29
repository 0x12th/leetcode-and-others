"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


def letter_combinations(self, digits: str) -> list[str]:
    if not digits:
        return []

    dct = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = []
    path = []

    def backtrack(idx: int) -> None:
        if idx == len(digits):
            res.append("".join(path))
            return

        for char in dct[digits[idx]]:
            path.append(char)
            backtrack(idx + 1)
            path.pop()

    backtrack(0)

    return res
