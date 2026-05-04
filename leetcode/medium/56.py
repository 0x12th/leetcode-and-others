def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    intervals.sort(key=lambda interval: interval[0])
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
