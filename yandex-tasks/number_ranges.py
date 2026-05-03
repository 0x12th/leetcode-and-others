"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, сокращая соседние по числовому ряду числа в диапазоны.

Примеры:
[1, 4, 5, 2, 9, 8, 11, 0, 3] => "0-5,8-9,11"
[1, 4, 3, 2] => "1-4"
[1, 4] => "1,4"
"""


def format_ranges(numbers: list[int]) -> str:
    if not numbers:
        return ""

    res = []
    sorted_numbers = sorted(numbers)
    first = last = sorted_numbers[0]

    for num in sorted_numbers[1:]:
        if num - last == 1:
            last = num
        else:
            res.append(str(last) if last == first else f"{first}-{last}")
            first = last = num

    res.append(str(last) if last == first else f"{first}-{last}")

    return ",".join(res)
