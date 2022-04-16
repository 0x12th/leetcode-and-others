# [2, 1, 3], [1, 2, 3] -> true
# [2, 1, 1, 3], [1, 2, 3] -> true
# [1, 1, 1, 3], [1, 3, 3] -> false
# [1, 2], [1, 2, 3] -> false


def is_subset(lst1: list[int], lst2: list[int]) -> bool:
    return set(lst1) == set(lst2)
