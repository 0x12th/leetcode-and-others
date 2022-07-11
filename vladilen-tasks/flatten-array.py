# [[1], [[2, 3]], [[[4]]]] -> [1, 2, 3, 4]


def flatten(arr: list) -> list:
    return [
        int(s) if s.isnumeric() else s
        for s in str(arr)
        if s not in (" ", "'", ",", "[", "]")
    ]
