"""
Даны два массива целых чисел длины N.
Для каждого K от 1 до N нужно посчитать количество общих элементов в первых K элементах обоих массивов.
Пересечение считается без учета кратности.

Пример:
a = [1, 2, 5, 2, 7, 9]
b = [2, 5, 8, 1, 9, 3]
result = [0, 1, 2, 3, 3, 4]
"""


def _prefix_intersection_count(a: list[int], b: list[int]) -> list[int]:
    res = []
    common = 0
    seen_a, seen_b = set(), set()

    for val_a, val_b in zip(a, b):
        if val_a not in seen_a:
            if val_a in seen_b:
                common += 1
            seen_a.add(val_a)

        if val_b not in seen_b:
            if val_b in seen_a:
                common += 1
            seen_b.add(val_b)

        res.append(common)

    return res


def prefix_intersection_count(a: list[int], b: list[int]) -> list[int]:
    res = []

    for i in range(len(a)):
        most_common = 0
        set_a = set(a[: i + 1])
        set_b = set(b[: i + 1])

        for val in set_a:
            if val in set_b:
                most_common += 1

        res.append(most_common)

    return res
