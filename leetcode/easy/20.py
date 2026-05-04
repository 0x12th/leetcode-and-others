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
