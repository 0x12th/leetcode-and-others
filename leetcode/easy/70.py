def climb_stairs(n: int) -> int:
    if n == 1:
        return 1

    step_one, step_two = 1, 2
    for _ in range(3, n + 1):
        step_one, step_two = step_two, step_one + step_two

    return step_two
