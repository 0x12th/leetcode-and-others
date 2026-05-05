"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
"""


def climb_stairs(n: int) -> int:
    if n == 1:
        return 1

    step_one, step_two = 1, 2
    for _ in range(3, n + 1):
        step_one, step_two = step_two, step_one + step_two

    return step_two
