def get_row(row_index: int) -> list[int]:
    row = [1]
    for _ in range(row_index):
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return row
