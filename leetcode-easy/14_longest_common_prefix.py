from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    result = []
    for z in zip(*strs):
        if len(set(z)) == 1:
            print(z)
            result.append(z[0])
        else:
            break
    return "".join(result)
