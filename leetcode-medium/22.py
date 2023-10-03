from typing import List


def generate_parenthesis(n: int) -> List[str]:
    result: List[str] = []

    def helper(left: int, right: int, s: str) -> None:
        if right == n:
            result.append(s)
            return
        if left < n:
            helper(left + 1, right, s + "(")
        if right < left:
            helper(left, right + 1, s + ")")

    helper(0, 0, "")

    return result
