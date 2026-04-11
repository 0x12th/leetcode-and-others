def longest_common_prefix(strs: list[str]) -> str:
    result = []
    for z in zip(*strs):
        if len(set(z)) == 1:
            result.append(z[0])
        else:
            break
    return "".join(result)
