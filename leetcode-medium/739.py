from typing import List


def daily_temperatures(t: List[int]) -> List[int]:
    result = [0] * len(t)
    stack: List[int] = []
    for i in range(len(t)):
        while stack and t[stack[-1]] < t[i]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result
