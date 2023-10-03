def is_happy(n: int) -> bool:
    if n == 1:
        return True
    if n == 4:
        return False
    return is_happy(sum([n**2 for n in [int(i) for i in str(n)]]))
