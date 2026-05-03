"""
Дан непустой массив из нулей и единиц.
Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив (пропустив) ровно один элемент массива.
Удалить один элемент из массива обязательно.

Пример:
assert max_ones([1, 1, 0, 1]) == 3
assert max_ones([1, 1, 0, 0, 1]) == 2
"""


def max_ones(nums: list[int]) -> int:
    max_ones = zeros = left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_ones = max(max_ones, right - left)

    return max_ones
