"""
   0    ->   90    ->   180   ->   270
[1,2,3]    [7,4,1]    [9,8,7]    [3,6,9]
[4,5,6] -> [8,5,2] -> [6,5,4] -> [2,5,8]
[7,8,9]    [9,6,3]    [3,2,1]    [1,4,7]
"""


def rotate_matrix_90_(source: list[list[int]]) -> list[list[int]]:
    return [list(_) for _ in list(zip(*reversed(source)))]


def rotate_matrix_90(source: list[list[int]]) -> list[list[int]]:
    return [
        [source[i][j] for i in range(len(source) - 1, -1, -1)]
        for j in range(len(source))
    ]


def rotate_matrix_180(source: list[list[int]]) -> list[list[int]]:
    return [
        [source[i][j] for j in range(len(source) - 1, -1, -1)]
        for i in reversed(range(len(source)))
    ]


def rotate_matrix_270(source: list[list[int]]) -> list[list[int]]:
    return [
        [source[i][j] for i in range(len(source))] for j in reversed(range(len(source)))
    ]
