"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""


def inserted(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    inserted: list[list[int]] = []
    intervals.append(new_interval)
    intervals.sort(key=lambda interval: interval[0])
    for interval in intervals:
        if not inserted or inserted[-1][1] < interval[0]:
            inserted.append(interval)
        else:
            inserted[-1][1] = max(inserted[-1][1], interval[1])
    return inserted
