import collections


def lengthOfLongestSubstring(s: str) -> int:
    left, right, result = 0, 0, 0
    dct = collections.defaultdict(bool)
    while right < len(s):
        if not dct[s[right]]:
            result = max(result, right - left + 1)
            dct[s[right]] = True
            right += 1
        else:
            dct[s[left]] = False
            left += 1
    return result
