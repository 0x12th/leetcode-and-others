# fibonacci(8) -> [1, 1, 2, 3, 5, 8, 13, 21]


def fib_0(n: int) -> list[int]:
    a, b = 0, 1
    lst = []
    for _ in range(n):
        a, b = b, a + b
        lst.append(a)
    return lst


def fib_1(n: int) -> list[int]:
    lst = [1, 1]
    for i in range(n - 2):
        lst.append(lst[i] + lst[i + 1])
    return lst


def fib_2(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a  # print(list(fib_2(n)))
