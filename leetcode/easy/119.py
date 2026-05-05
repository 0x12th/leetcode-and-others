"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: rowIndex = 3
Output: [1,3,3,1]
"""


def get_row(row_index: int) -> list[int]:
    row = [1]
    for _ in range(row_index):
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return row
