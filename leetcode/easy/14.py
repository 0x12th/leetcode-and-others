"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longest_common_prefix(strs: list[str]) -> str:
    result = []
    for z in zip(*strs):
        if len(set(z)) == 1:
            result.append(z[0])
        else:
            break
    return "".join(result)
