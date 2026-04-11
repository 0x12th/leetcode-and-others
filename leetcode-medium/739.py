def daily_temperatures(t: list[int]) -> list[int]:
    result = [0] * len(t)
    stack: list[int] = []
    for i in range(len(t)):
        while stack and t[stack[-1]] < t[i]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result
