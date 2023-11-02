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
