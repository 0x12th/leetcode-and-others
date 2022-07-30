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


def length_of_longest_substring_2(s: str) -> int:
    st = set()
    left, result = 0, 0
    for right, value in enumerate(s):
        while value in st:
            st.remove(s[left])
            left += 1
        st.add(value)
        result = max(right - left + 1, result)
    return result
