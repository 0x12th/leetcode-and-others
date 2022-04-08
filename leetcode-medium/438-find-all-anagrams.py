from collections import Counter, defaultdict
from typing import List


def findAnagrams_1(s: str, p: str) -> List[int]:
    start = []
    window_str = ''
    start_count = 0
    for letter in s:
        window_str += letter
        if len(window_str) == len(p):
            if sorted(window_str) == sorted(p):
                start.append(start_count)
            window_str = window_str[1:]
            start_count += 1
    return start


def findAnagrams_2(s: str, p: str) -> List[int]:
    pattern = Counter(p)
    result = []
    window = defaultdict(int)
    start_point = 0
    for end in range(len(s)):
        window[s[end]] += 1
        print(window)
        if end - start_point + 1 == len(p):
            if window == pattern:
                print(window)
                result.append(start_point)
            window[s[start_point]] -= 1
            if window[s[start_point]] == 0:
                del window[s[start_point]]
            start_point += 1
    return result
