from typing import List


def letterCasePermutation(s: str) -> List[str]:
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
