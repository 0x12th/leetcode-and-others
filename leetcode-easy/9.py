def is_palindrome(x: int) -> bool:
    return list(str(x)) == list(reversed(str(x)))
