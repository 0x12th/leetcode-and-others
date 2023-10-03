from typing import List


def inserted(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    inserted: List[List[int]] = []
    intervals.append(new_interval)
    intervals.sort(key=lambda interval: interval[0])
    for interval in intervals:
        if not inserted or inserted[-1][1] < interval[0]:
            inserted.append(interval)
        else:
            inserted[-1][1] = max(inserted[-1][1], interval[1])
    return inserted
