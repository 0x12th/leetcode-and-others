from typing import List


def count_points(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    result = [0] * len(queries)
    for q, query in enumerate(queries):
        for point in points:
            if (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2 <= query[2] ** 2:
                result[q] += 1
    return result
