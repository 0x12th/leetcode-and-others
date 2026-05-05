"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
"""


def is_valid(s: str) -> bool:
    stack = []
    char_deque = {"(": ")", "{": "}", "[": "]"}
    for bracket in s:
        if bracket in char_deque:
            stack.append(bracket)
        else:
            if len(stack) == 0 or bracket != char_deque[stack.pop()]:
                return False
    return len(stack) == 0
