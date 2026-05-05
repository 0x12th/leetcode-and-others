"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""


def daily_temperatures(t: list[int]) -> list[int]:
    result = [0] * len(t)
    stack: list[int] = []
    for i in range(len(t)):
        while stack and t[stack[-1]] < t[i]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result
