import collections


def min_window(s: str, t: str) -> str:
    dct = collections.Counter(t)
    left, size = 0, 0
    result = [0, 10**5]

    for right, value in enumerate(s):
        if value in dct:
            dct[value] -= 1

            if dct[value] == 0:
                size += 1

        while size == len(dct):
            if right - left < result[1] - result[0]:
                result[0], result[1] = left, right

            if s[left] in dct:
                if dct[s[left]] == 0:
                    size -= 1
                dct[s[left]] += 1

            left += 1

    if result[1] == 10**5:
        return ""

    return s[result[0]: result[1] + 1]
