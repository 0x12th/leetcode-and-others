from typing import List


def dailyTemperatures(t: List[int]) -> List[int]:
    result = [0] * len(t)
    stack = []
    for i in range(len(t)):
        while stack and t[stack[-1]] < t[i]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result
